from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from flask_mysqldb import MySQL
from random import randint
from flask_mail import *
from MySQLdb.cursors import Cursor

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")


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
        if user != None and user[4] == 1:

            # Logando o Usuário
            if user:
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[2]
                return redirect(url_for('feed'))

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
        turma = request.form['turma']
        nome = request.form['nome']
        email = request.form['e-mail']
        senha = request.form['senha']

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
        cursor.execute(
            'INSERT into participa (tur_id, user_id) values(%s, %s) ', (turma, usuario[0]))
        mysql.connection.commit()

    # Inserindo o ID do usuário e o cargo padrão na tabela cargo_user
        cursor.execute(
            'INSERT into exerce (car_id, user_id) values("5", %s) ', (usuario[0],))
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


@app.route('/area-usuario/')
def myinfo():
    # Checando se o usuário está logado.
    if 'loggedin' in session:
        user_id = session['id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE user_id = %s", (user_id,))
        usuario = cursor.fetchone()

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM participa WHERE user_id = %s", (user_id,))
        turma_id = cursor.fetchall()

        id_curso = []
        for tur in turma_id:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT cur_id FROM turma where tur_id = %s", (tur[0],))
            cur_id = cursor.fetchall()
            id_curso.append(cur_id[0])


        cursos = []
        for cur in id_curso:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT cur_nome FROM curso where cur_id = %s", (cur[0],))
            curso = cursor.fetchall()
            cursos.append(curso[0])
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT car_id FROM exerce WHERE user_id = %s", (user_id,))
        cargo_id = cursor.fetchone()

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cargo where car_id = %s", (cargo_id,))
        cargo = cursor.fetchone()

        return render_template('my_info.html', usuario=usuario, cursos=cursos, cargo=cargo)

    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

# função para puxar filtros do banco de dados


def listarCursos():
    cur = mysql.connection.cursor()
    cur.execute("select cur_id, cur_nome from curso")
    return cur.fetchall()


def listarCargos():
    cur = mysql.connection.cursor()
    cur.execute("select car_id, car_nome from cargo")
    return cur.fetchall()

###### Rota para a página do feed ######


@app.route('/feed/')
def feed():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Puxando o ID do usuário a partir de sua Sessão do Login.
        user_id = session['id']
        # Verificando o cargo do usuário
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * from exerce where user_id = %s', (user_id,))
        cargo_user = cursor.fetchone()

        # Verificando se o Cargo do usuário pode ou não enviar informações.
        if cargo_user != None and cargo_user[0] == 5:
            perm = 0
        elif cargo_user != None and (cargo_user[0] == 1 or cargo_user[0] == 3):
            perm = 2
        else:
            perm = 1

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * from publica where user_id = %s", (user_id,))
        autoria = cursor.fetchall()

    # Puxando informações do banco de dados.
        cursor = mysql.connection.cursor()
        info = cursor.execute(
            "SELECT post_id,post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, car_nome, post_remetente,post_anexo FROM feed ORDER BY post_data DESC")
        if info > 0:
            infoDetails = cursor.fetchall()

            return render_template("feed.html", infoDetails=infoDetails, perm=perm, autoria=autoria, cursos=listarCursos(), cargos=listarCargos())
        else:
            return render_template("feed.html", cursos=listarCursos(), perm=perm, cargos=listarCargos())

    # Redirecionando o Usuário para a página de login caso ele não esteja logado.
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página de envio de informações ######


@app.route('/envio-informacao/', methods=['GET', 'POST'])
def envio_informacao():
    # Checando se o usuário está logado.
    if 'loggedin' in session:

        # Puxando o ID do usuário a partir de sua Sessão do Login.
        id_usuario = session['id']
        # Verificando o cargo do usuário
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * from exerce where user_id = %s', (id_usuario,))
        cargo_user = cursor.fetchone()

        # Verificando se o Cargo do usuário pode ou não enviar informações.
        if cargo_user != None:
            if cargo_user[0] == 5:
                perm = 0
            elif cargo_user[0] == 1 or cargo_user[0] == 3:
                perm = 2
            else:
                perm = 1
        else:
            perm = 1

        # Solicitando informações da mensagem no formulário.
        if request.method == 'POST':
            remetente = session['username']
            titulo = request.form['titulo']
            data_inclusao = datetime.now()
            assunto = request.form['assunto']
            turma = request.form.getlist('turma')
            des = request.form.getlist('destinatario')
            mensagem = request.form['mensagem']
            destinatario = ",".join(str(x) for x in des)

        # Inserindo informações na tabela feed.
            cursor = mysql.connection.cursor()
            cursor.execute("insert into feed (post_data, post_assunto, post_titulo, post_mensagem, post_remetente,car_nome) values (%s, %s, %s, %s, %s, %s)",
                           (data_inclusao, assunto, titulo, mensagem, remetente, destinatario))
            mysql.connection.commit()

        # Checando se as informações foram salvas.
            cursor = mysql.connection.cursor()
            cursor.execute("select * from feed where post_assunto = %s and post_titulo = %s and post_mensagem = %s and post_remetente = %s and car_nome = %s",
                           (assunto, titulo, mensagem, remetente, destinatario))
            info = cursor.fetchone()

            for tur in turma:
                post_id = info[0]
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "insert into recebe (post_id,tur_id) values(%s, %s)", (post_id, tur))
                mysql.connection.commit()

        # Inserindo ID do post e ID do usuario na tabela "publica"

            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO publica (user_id,post_id) values (%s,%s)", (id_usuario, post_id))
            mysql.connection.commit()

        # Redirecionando o Usuário para a página de Feed caso as informações foram salvas.
            if info:
                return redirect(url_for('feed'))
        return render_template('send-info.html', perm=perm, cursos=listarCursos(), cargos=listarCargos())
    # Redirecionando o Usuário para a página de login caso ele não esteja logado.
    else:
        flash('Faça o login antes de continuar.')
        return redirect(url_for('login'))

###### Rota para a página de recuperação de senha ######


@ app.route('/recuperar-senha/', methods=['GET', 'POST'])
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


@ app.route('/alterar-senha/', methods=['GET', 'POST'])
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


@ app.route("/editar-usuario/", methods=['GET', "POST"])
def edit():
    # Checando se o usuário está logado.
    if 'loggedin' in session:
        # Puxando o ID do usuário a partir de sua Sessão do Login.
        id_usuario = session['id']
        # Verificando o cargo do usuário
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * from exerce where user_id = %s', (id_usuario,))
        cargo_user = cursor.fetchone()

        # Verificando se o Cargo do usuário pode ou não enviar informações.
        if cargo_user[0] == 5:
            perm = 0
        elif cargo_user[0] == 1 or cargo_user[0] == 3:
            perm = 2
        else:
            perm = 1

        # Solicitando informações do usuário a ser alterado e suas mudanças (Cargo e Curso).
        if request.method == "POST":
            email = request.form["e-mail"]
            cargo = request.form["cargo"]
            turma = request.form.getlist("turma")

        # Selecionando o ID do usuário inserido.
            cursor = mysql.connection.cursor()
            cursor.execute(
                'SELECT user_id from usuario WHERE user_email = %s', (email,))
            user = cursor.fetchone()

        # Alterando os cursos e o cargo do usuário se solicitado.
            if user:
                cursor = mysql.connection.cursor()
                cursor.execute(
                    'UPDATE exerce SET car_id = %s WHERE user_id = %s', (cargo, user))
                for x in turma:
                    mysql.connection.commit()
                    cursor = mysql.connection.cursor()
                    cursor.execute(
                        'INSERT INTO participa (tur_id,user_id) values (%s, %s)', (x, user))
                    mysql.connection.commit()

                return redirect(url_for('feed'))

        # Caso de usuário não encontrado é emitido uma mensagem
            else:
                flash('Usuário não encontrado!')
        return render_template("editar_usuario.html", perm=perm)

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


@app.route('/excluir-post/<id>')
def excluir(id):
    id_post = id

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE  FROM publica WHERE post_id = %s", (id_post,))
    mysql.connection.commit()

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE  FROM recebe WHERE post_id = %s", (id_post,))
    mysql.connection.commit()

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE  FROM feed WHERE post_id = %s", (id_post,))
    mysql.connection.commit()

    return redirect(url_for('feed'))


@app.route('/editar-post/<id>', methods=['GET', 'POST'])
def editar_post(id):
    # Puxando o ID do usuário a partir de sua Sessão do Login.
    id_usuario = session['id']
    # Verificando o cargo do usuário
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from exerce where user_id = %s', (id_usuario,))
    cargo_user = cursor.fetchone()

    # Verificando se o Cargo do usuário pode ou não enviar informações.
    if cargo_user[0] == 5:
        perm = 0
    elif cargo_user[0] == 1 or cargo_user[0] == 3:
        perm = 2
    else:
        perm = 1

    id_post = id
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM feed WHERE post_id = %s", (id_post,))
    info = cursor.fetchone()
    if request.method == 'POST':

        remetente = session['username']
        titulo = request.form['titulo']
        assunto = request.form['assunto']
        turma = request.form['turma']
        des = request.form.getlist('destinatario')
        mensagem = request.form['mensagem']
        destinatario = ",".join(str(x) for x in des)

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE feed SET post_titulo = %s, post_assunto = %s, post_mensagem = %s,  car_nome = %s WHERE post_id = %s",
                       (titulo, assunto, mensagem, destinatario, id_post))

                    
        return redirect(url_for('feed'))

    return render_template("send-info.html", perm=perm, info=info)


def existemFiltrosSelecionados():
    return assuntoFoiSelecionado() or turmaFoiSelecionada() or destinatarioFoiSelecionado()

def assuntoFoiSelecionado():
    return request.form['hidden_assunto'] != ""

def turmaFoiSelecionada():
    return request.form['hidden_turma'] != ""

def destinatarioFoiSelecionado():
    return request.form['hidden_destinatario'] != ""

def getValoresSelecionadosParaSQL(valorCampoHidden):

    split = valorCampoHidden.split(',')

    valoresSelecionados = ""

    for valor in split:
        if(valoresSelecionados == ""):
            valoresSelecionados = "'" + valor + "'"
        else:
            valoresSelecionados = valoresSelecionados + ", '" + valor + "' "

    return valoresSelecionados


@app.route("/filtrar_feed_ajax", methods=["POST", "GET"])
def filtrar_feed_ajax():
    user_id = session['id']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from publica where user_id = %s", (user_id,))
    autoria = cursor.fetchall()
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        

        

        sql = "SELECT post_id,post_titulo, DATE_FORMAT(post_data, '%d/%m/%Y'), post_assunto, post_mensagem, car_nome, post_remetente,post_anexo FROM feed"

        assuntosSelecionados = getValoresSelecionadosParaSQL(request.form['hidden_assunto'])
        turmasSelecionadas = getValoresSelecionadosParaSQL(request.form['hidden_turma'])
        destinatariosSelecionados = getValoresSelecionadosParaSQL(request.form['hidden_destinatario'])

        
        if(existemFiltrosSelecionados()):
            sql = sql + " WHERE "
            if(assuntoFoiSelecionado()):
                sql = sql + " post_assunto IN (" + assuntosSelecionados + ") "

            if(turmaFoiSelecionada()):

                if(assuntoFoiSelecionado()):
                    sql = sql + " AND "

                sql = sql + " post_id IN (SELECT r.post_id FROM recebe r WHERE r.tur_id IN (" + turmasSelecionadas + ") )"

            if(destinatarioFoiSelecionado()):

                print("Cargos selecionados: " + destinatariosSelecionados)

                if(assuntoFoiSelecionado() or turmaFoiSelecionada()):
                    sql = sql + " AND "
                sql = sql + " 1 = 1 " ### TODO criar SQL para filtrar com base nos destinatarios selecionados

            sql = sql + " ORDER BY post_data DESC"

        else:
            sql = sql + " ORDER BY post_data DESC"

        info = cursor.execute(sql)
        infoDetails = cursor.fetchall()

    return render_template('conteudo-div-feed.html', infoDetails=infoDetails, autoria=autoria)


if __name__ == '__main__':
    app.run()