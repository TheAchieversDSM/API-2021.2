from flask import Flask, render_template,request,redirect,url_for,flash,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TheAchieversDSM'    

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'api_fatec'

mysql = MySQL(app)



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

        if user:
            session['loggedin'] = True
            session['id'] = user[0]
            session['username'] = user[3]
            return redirect(url_for('feed_adm'))

        else:
            flash("Senha/Email inválido ou usuário não registrado","erro")

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
        if status:
            flash("Cadastrado com sucesso","info")
            return redirect(url_for('login'))
    return render_template('cadastro.html')

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