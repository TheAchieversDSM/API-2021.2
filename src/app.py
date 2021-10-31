from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from random import randint
from flask_mail import *
from MySQLdb.cursors import Cursor

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TheAchieversDSM'    

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fatec_api'

mysql = MySQL(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'the.achieversAPI@gmail.com'
app.config['MAIL_PASSWORD'] = 'theachieversFATEC'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

code = str(randint(000000, 999999))

@app.route('/',methods=['GET','POST'])
def login():
    # Solicitando informações do usuário no formulário.
    if request.method == 'POST':
        email = request.form['e-mail']
        senha = request.form['senha']

    # Checando se usuário está cadastrado
        cursor = mysql.connection.cursor()
        cursor.execute('select * from usuario WHERE email = %s and senha = %s', (email,senha))
        user = cursor.fetchone()

        if user[4] == 1:
            if user:
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[3]
                return redirect(url_for('feed_adm'))

            else:
                flash("Senha/Email inválido ou usuário não registrado","erro")
        else:
            flash('Confirme seu e-mail antes.')
            return redirect(url_for('confirmacao', email=user[1]))

    return render_template('login.html')

@app.route('/cadastro/',methods=['GET','POST'])
def cadastro():
    # Solicitando informações do usuário no formulário.
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['e-mail']
        senha = request.form['senha']

    # Inserindo informações na tabela Usuário.
        cursor = mysql.connection.cursor()
        cursor.execute("insert into usuario(email,senha,nome) values (%s, %s,%s)", (email,senha,nome))
        mysql.connection.commit()
        
    # Checando se as informações foram salvas.
        cursor.execute('select * from usuario WHERE email = %s and senha = %s ', (email,senha))
        status = cursor.fetchone()

        if status[4] == 0:
            msg = Message('Confirme seu e-mail', sender = 'the.achieversAPI@gmail.com', recipients = [email])

            msg.html = "<h1 align='center' style='background-color:#ab101a'>Confirme seu e-mail!</h1> <p align='center' style='background-color:#C4C4C4'>Segue o código para verificação do seu cadastro para posterior acesso ao site de informações da FATEC:</p> <p align='center' style='background-color:#ab101a'>{}</p> <p align='center' style='background-color:#C4C4C4'>E-mail automático, favor não responder.</p>".format(code)
            mail.send(msg)    
            return redirect(url_for('confirmacao', email = email))

    return render_template('cadastro.html', code = code)

@app.route('/confirme-seu-email/', methods=['GET', 'POST'])
def confirmacao():
    if request.method == 'POST':
        codigo = request.form['cod']
        email = request.args.get('email')
        if codigo == code:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE usuario SET confirmacao='1' WHERE email = %s", (email,))
            mysql.connection.commit()
            return redirect(url_for('login'))
    return render_template('confirmacao.html')

@app.route('/feed/')
def feed():
    if 'loggedin' in session:

        cur = mysql.connection.cursor()

        # Puxando informações do banco de dados.
        info = cur.execute("SELECT titulo, destinatario, DATE_FORMAT(data_inclusao, '%d/%m/%Y'), assunto, curso_id, mensagem FROM feed")

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
        info = cur.execute("SELECT titulo, remetente, destinatario, DATE_FORMAT(data_inclusao, '%d/%m/%Y' ), assunto, curso_id, mensagem FROM feed")

        if info > 0:
            infoDetails = cur.fetchall()
            return render_template("feed-adm.html", infoDetails=infoDetails)
        else:
            return render_template("feed-adm.html")
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

@app.route('/envio-informacao/', methods=['GET','POST'])
def envio_informacao():
    if 'loggedin' in session:

        # Solicitando informações da mensagem no formulário.
        if request.method == 'POST': 
            remetente = session['username']
            titulo = request.form['titulo']
            data_inclusao = request.form['data']
            assunto = request.form['assunto']
            curso = request.form['curso']
            des = request.form.getlist('destinatario')
            mensagem = request.form['mensagem']
            destinatario= ",".join(str(x) for x in des)

        # Inserindo informações na tabela feed.
            cursor = mysql.connection.cursor()
            cursor.execute("insert into feed(data_inclusao, assunto, destinatario, curso_id, remetente, titulo, mensagem) values (%s, %s, %s, %s, %s, %s, %s)", (data_inclusao,assunto,destinatario,curso, remetente,titulo,mensagem))
            mysql.connection.commit()

        # Checando se as informações foram salvas.
            cursor.execute('select * from feed WHERE data_inclusao = %s and assunto = %s and curso_id = %s and remetente = %s and titulo = %s and mensagem = %s and destinatario = %s', (data_inclusao,assunto,curso, remetente,titulo,mensagem,destinatario))
            status = cursor.fetchone()
        
            if status:
                return redirect(url_for('feed_adm'))
        return render_template('send-info.html')
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))
        

if __name__ == '__main__':
    app.run()