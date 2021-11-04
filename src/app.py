from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date
from flask_mysqldb import MySQL
from random import randint
from flask_mail import *
from MySQLdb.cursors import Cursor

app = Flask(__name__)


###### Configuração FlaskMySQLdb ######
app.config['SECRET_KEY'] = 'TheAchieversDSM'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'fatec_api'

mysql = MySQL(app)

###### Configuração Flask_Mail ######
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'the.achieversAPI@gmail.com'
app.config['MAIL_PASSWORD'] = 'theachieversFATEC'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

###### Geração de código para confirmar Email ######
code = str(randint(000000, 999999))


###### Rota para a página de Login ######

@app.route('/', methods=['GET', 'POST'])
def login():
    # Solicitando informações do usuário no formulário
    if request.method == 'POST':
        email = request.form['e-mail']
        senha = request.form['senha']

    # Checando se usuário está cadastrado
        cursor = mysql.connection.cursor()
        cursor.execute(
            'select * from usuario WHERE user_email = %s and user_senha = %s', (email, senha))
        user = cursor.fetchone()

        # Checando se o usuário já confirmou seu email
        if user[4] == 1:

            # Logando o Usuário
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

###### Rota para a página de Cadastro ######


@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    # Solicitando informações do usuário no formulário.
    if request.method == 'POST':
        curso = request.form['curso']
        semestre = request.form['semestre']
        nome = request.form['nome']
        email = request.form['e-mail']
        senha = request.form['senha']

    # Checando a turma selecionada pelo usuário
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT tur_id from turma WHERE tur_semestre = %s and cur_id = %s", (semestre, curso))
        turma = cursor.fetchone()

    # Inserindo informações na tabela Usuário.
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT into usuario(user_email, user_nome, user_senha) values (%s, %s,%s)", (email, nome, senha))
        mysql.connection.commit()

    # Checando se as informações foram salvas.
        cursor.execute(
            'SELECT * from usuario WHERE user_email = %s and user_senha = %s ', (email, senha))
        usuario = cursor.fetchone()

    # Inserindo o ID do usuário e sua respectiva turma na tabela turma_user
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT into turma_user (tur_id, user_id) values(%s, %s) ', (turma, usuario[0]))
        mysql.connection.commit()

    # Inserindo o ID do usuário e o cargo padrão na tabela cargo_user
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT into cargo_user (car_id, user_id) values("5", %s) ', (usuario[0],))
        mysql.connection.commit()

    # Enviando email de confirmação para o email inserido pelo o usuário
        if usuario[4] == 0:
            msg = Message('Confirme seu e-mail',
                          sender='the.achieversAPI@gmail.com', recipients=[email])

            msg.html = "<h1 align='center' style='background-color:#ab101a'>Confirme seu e-mail!</h1> <p align='center' style='background-color:#c4c4c4'>Segue o código para verificação do seu cadastro para posterior acesso ao site de informações da FATEC:</p> <h2 align='center' style='background-color:#ab101a'>{}</h2> <p align='center' style='background-color:#c4c4c4'>E-mail automático, favor não responder.</p>".format(
                code)
            mail.send(msg)
            return redirect(url_for('confirmacao', email=email))

    return render_template('cadastro.html', code=code)

###### Rota para a página de Confirmação de email ######


@app.route('/confirme-seu-email/', methods=['GET', 'POST'])
def confirmacao():
    # Solicitando informações do formulário
    if request.method == 'POST':
        codigo = request.form['cod']
        email = request.args.get('email')
        rec = request.args.get('rec')

     # Checando se o código do formulário é o mesmo que o código enviado para o email do usuário.
        if codigo == code:

         # Checagem para o caso de solicitação de nova senha o usuario é redirecionado após a confirmação do email
            if rec == 'True':
                return redirect(url_for('novasenha', email=email))

         # Usuário confirmado no banco de dados.
            else:
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "UPDATE usuario SET confirmacao='1' WHERE user_email = %s", (email,))
                mysql.connection.commit()
            return redirect(url_for('login'))
    return render_template('confirmacao.html')

###### Rota para a página do feed ######

@app.route('/feed/')
def feed():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Puxando informações do banco de dados.
        cur = mysql.connection.cursor()
        info = cur.execute(
            "SELECT post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, tur_semestre, cur_id, car_id FROM feed ORDER BY post_data")

    # Enviando Informações para o template.
        if info > 0:
            infoDetails = cur.fetchall()
            return render_template("feed.html", infoDetails=infoDetails)
        else:
            return render_template("feed.html")

    # Redirecionando o Usuário para a página de login caso ele não esteja logado.
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página do feed do adm ######

@app.route('/feed-adm/')
def feed_adm():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Puxando o ID do usuário a partir de sua Sessão do Login.
        user_id = session['id']

    # Puxando informações do banco de dados.
        cur = mysql.connection.cursor()
        info = cur.execute(
            "SELECT post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, tur_semestre, cur_id, car_id FROM feed ORDER BY post_data DESC")
        if info > 0:
            infoDetails = cur.fetchall()

         # Verificando o cargo do usuário
            cursor = mysql.connection.cursor()
            cursor.execute(
                'SELECT car_id from cargo_user where user_id = %s', (user_id,))
            cargo_user = cursor.fetchone()

        # Verificando se o Cargo do usuário pode ou não enviar informações.
            if cargo_user == 1 or cargo_user == 2 or cargo_user == 3 or cargo_user == 4:
                cargo_user = True
            else:
                cargo_user = False

            return render_template("feed-adm.html", infoDetails=infoDetails, cargo_user=cargo_user)
        else:
            return render_template("feed-adm.html")

    # Redirecionando o Usuário para a página de login caso ele não esteja logado.
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página de envio de informações ######


@app.route('/envio-informacao/', methods=['GET', 'POST'])
def envio_informacao():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Solicitando informações da mensagem no formulário.
        if request.method == 'POST':
            remetente = session['username']
            titulo = request.form['titulo']
            data_inclusao = date.today()
            assunto = request.form['assunto']
            curso = request.form['curso']
            semestre = request.form['semestre']
            des = request.form.getlist('destinatario')
            mensagem = request.form['mensagem']
            destinatario = ",".join(str(x) for x in des)

        # Inserindo informações na tabela feed.
            cursor = mysql.connection.cursor()
            cursor.execute("insert into feed (post_data, post_assunto, post_titulo, post_mensagem, cur_id, tur_semestre, post_remetente,car_id) values (%s, %s, %s, %s, %s, %s, %s,%s)",
                           (data_inclusao, assunto, titulo, mensagem, curso, semestre, remetente, destinatario))
            mysql.connection.commit()

        # Checando se as informações foram salvas.
            cursor.execute('select * from feed WHERE post_data = %s and post_assunto = %s and cur_id = %s and post_remetente = %s and post_titulo = %s and post_mensagem = %s and car_id= %s',
                           (data_inclusao, assunto, curso, remetente, titulo, mensagem, destinatario))
            status = cursor.fetchone()

        # Redirecionando o Usuário para a página de Feed caso as informações foram salvas.
            if status:
                return redirect(url_for('feed_adm'))
        return render_template('send-info.html')
    # Redirecionando o Usuário para a página de login caso ele não esteja logado.
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página de recuperação de senha ######


@app.route('/recuperar-senha/', methods=['GET', 'POST'])
def recsenha():
    if request.method == 'POST':
        # Solicitando o email do usuario do formulario.
        email = request.form['e-mail']

    # Indicando para a página de confirmação de email quea  solicitação Veio da página de recuperação de senha.
        rec = True

    # Checando e pegando o email do usuário do banco de dados.
        cursor = mysql.connection.cursor()
        cursor.execute(
            'select * from usuario WHERE user_email = %s ', (email,))
        usuario = cursor.fetchone()

    # Enviando um email para confirmar se o usuário solicitou a alteração.
        if usuario:
            msg = Message('Alteração de senha',
                          sender='the.achieversAPI@gmail.com', recipients=[email])
            msg.html = "<h1 align='center' style='background-color:#ab101a'>Alterar Senha!</h1> <p align='center' style='background-color:#c4c4c4'>Segue o código para verificação do seu cadastro para posterior alteração de senha:</p> <h2 align='center' style='background-color:#ab101a'>{}</h2> <p align='center' style='background-color:#c4c4c4'>E-mail automático, favor não responder.</p>".format(
                code)
            mail.send(msg)
            return redirect(url_for('confirmacao', email=email, rec=rec))

    # Caso de email não confirmado, redirecionar para a página de Login.
        else:
            flash('Email não cadastrado!')
            return redirect(url_for('login'))
    return render_template('recsenha.html')

###### Rota para a página de alteração de senha ######


@app.route('/alterar-senha/', methods=['GET', 'POST'])
def novasenha():
    if request.method == 'POST':
        # Solicitando email (argumentos da url) e senha (formulário)
        email = request.args.get('email')
        senha = request.form['senha']

    # Atualizando a senha do usuário na tabela do banco de dados
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE usuario SET user_senha = %s WHERE user_email = %s", (senha, email))
        mysql.connection.commit()

    # Redirecionando para Login.
        return redirect(url_for('login'))
    return render_template('altersenha.html')

###### Rota para a página de edição de usuário ######


@app.route("/editar-usuario/", methods=['GET', "POST"])
def edit():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Solicitando informações do usuário a ser alterado e suas mudanças (Cargo e Curso).
        if request.method == "POST":
            email = request.form["e-mail"]
            cargo = request.form["Cargo"]
            turma = request.form["Turma"]

        # Selecionando o ID do usuário inserido.
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT user_id from usuario WHERE email = %s',
                           (email,))
            user = cursor.fetchone()

        # Alterando os cursos e o cargo do usuário se solicitado.
            if user:
                cursor = mysql.connection.cursor()
                cursor.execute(
                    'UPDATE cargo_user SET car_id = %s WHERE user_id = %s', (cargo, user))

                mysql.connection.commit()
                cursor = mysql.connection.cursor()
                cursor.execute(
                    'UPDATE turma_user SET tur_id = %s WHERE user_id = %s', (turma, user))

                mysql.connection.commit()

                return redirect(url_for('feed_adm'))

        # Caso de usuário não encontrado é emitido uma mensagem
            else:
                flash('Usuário não encontrado!')
        return render_template("editar_usuario.html")

    # Redirecionando o Usuário para a página de login caso ele não esteja logado
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página de alteração de senha ######


@app.route('/logout')
def logout():
    # Deslogando o usuário da Sessão.
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
