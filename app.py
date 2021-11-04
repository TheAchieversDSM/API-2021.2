from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from random import randint
from flask_mail import *
from MySQLdb.cursors import Cursor

app = Flask(__name__, template_folder="src/templates",static_folder="src/static")

app.config['SECRET_KEY'] = 'TheAchieversDSM'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'fatec_api'

mysql = MySQL(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'the.achieversAPI@gmail.com'
app.config['MAIL_PASSWORD'] = 'theachieversFATEC'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

code = str(randint(000000, 999999))

@app.route('/', methods=['GET', 'POST'])
def login():
    # Solicitando informações do usuário no formulário.
    if request.method == 'POST':
        email = request.form['e-mail']
        senha = request.form['senha']

    # Checando se usuário está cadastrado
        cursor = mysql.connection.cursor()
        cursor.execute(
            'select * from usuario WHERE user_email = %s and user_senha = %s', (email, senha))
        user = cursor.fetchone()

        if user[4] == 1:
            if user:
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[2]
                return redirect(url_for('feed_adm'))

            else:
                flash("Senha/Email inválido ou usuário não registrado", "erro")
        else:
            flash('Confirme seu e-mail antes.')
            return redirect(url_for('confirmacao', email=user[1]))

    return render_template('login.html')

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    # Solicitando informações do usuário no formulário.
    if request.method == 'POST':
        curso = request.form['curso']
        semestre = request.form['semestre']
        nome = request.form['nome']
        email = request.form['e-mail']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT tur_id from turma WHERE tur_semestre = %s and cur_id = %s", (semestre, curso))
        turma = cursor.fetchone()

    # Inserindo informações na tabela Usuário.
        cursor = mysql.connection.cursor()
        cursor.execute(
            "insert into usuario(user_email, user_nome, user_senha) values (%s, %s,%s)", (email, nome, senha))
        mysql.connection.commit()

    # Checando se as informações foram salvas.
        cursor.execute(
            'select * from usuario WHERE user_email = %s and user_senha = %s ', (email, senha))
        usuario = cursor.fetchone()

        cursor = mysql.connection.cursor()
        cursor.execute(
            'insert into turma_user (tur_id, user_id) values(%s, %s) ', (turma, usuario[0]))
        mysql.connection.commit()

        if usuario[4] == 0:
            msg = Message('Confirme seu e-mail',
                          sender='the.achieversAPI@gmail.com', recipients=[email])

            msg.html = "<h1 align='center' style='background-color:#ab101a'>Confirme seu e-mail!</h1> <p align='center' style='background-color:#c4c4c4'>Segue o código para verificação do seu cadastro para posterior acesso ao site de informações da FATEC:</p> <h2 align='center' style='background-color:#ab101a'>{}</h2> <p align='center' style='background-color:#c4c4c4'>E-mail automático, favor não responder.</p>".format(
                code)
            mail.send(msg)
            return redirect(url_for('confirmacao', email=email))

    return render_template('cadastro.html', code=code)


@app.route('/confirme-seu-email/', methods=['GET', 'POST'])
def confirmacao():
    if request.method == 'POST':
        codigo = request.form['cod']
        email = request.args.get('email')
        if codigo == code:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "UPDATE usuario SET confirmacao='1' WHERE user_email = %s", (email,))
            mysql.connection.commit()
            return redirect(url_for('login'))
    return render_template('confirmacao.html')

@app.route('/feed/')
def feed():
    if 'loggedin' in session:

        cur = mysql.connection.cursor()

        # Puxando informações do banco de dados.
        info = cur.execute(
            "SELECT post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, tur_semestre, cur_id, car_id FROM feed")

        if info > 0:
            infoDetails = cur.fetchall()
            return render_template("feed.html", infoDetails=infoDetails)
        else:
            return render_template("feed.html")
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

@app.route('/feed-adm/')
def feed_adm():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()

        # Puxando informações do banco de dados.
        info = cur.execute(
            "SELECT post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, tur_semestre, cur_id, car_id FROM feed")

        if info > 0:
            infoDetails = cur.fetchall()
            return render_template("feed-adm.html", infoDetails=infoDetails)
        else:
            return render_template("feed-adm.html")
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

@app.route('/envio-informacao/', methods=['GET', 'POST'])
def envio_informacao():
    if 'loggedin' in session:

        # Solicitando informações da mensagem no formulário.
        if request.method == 'POST':
            remetente = session['username']
            titulo = request.form['titulo']
            data_inclusao = request.form['data']
            assunto = request.form['assunto']
            curso = request.form['curso']
            semestre = request.form['semestre']
            des = request.form.getlist('destinatario')
            mensagem = request.form['mensagem']
            destinatario = ",".join(str(x) for x in des)

        # Inserindo informações na tabela feed.
            cursor = mysql.connection.cursor()
            cursor.execute("insert into feed (post_data, post_assunto, post_titulo, post_mensagem, cur_id, tur_semestre, des) values (%s, %s, %s, %s, %s, %s, %s)", (data_inclusao, assunto, titulo, mensagem, curso, semestre, remetente))
            mysql.connection.commit()

        # Checando se as informações foram salvas.
            cursor.execute('select * from feed WHERE data_inclusao = %s and assunto = %s and curso_id = %s and remetente = %s and titulo = %s and mensagem = %s and destinatario = %s', (data_inclusao, assunto, curso, remetente, titulo, mensagem, destinatario))
            status = cursor.fetchone()

            if status:
                return redirect(url_for('feed_adm'))
        return render_template('send-info.html')
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()