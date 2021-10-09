from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '20210618'
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
        conta = cursor.fetchone()
        if conta:
            return redirect(url_for('feed'))
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
            return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/feed/')
def feed():
    cur = mysql.connection.cursor()

    # Puxando informações do banco de dados.
    info = cur.execute("SELECT titulo, destinatario, data_inclusao, assunto, curso_id, mensagem FROM feed")

    if info > 0:
        infoDetails = cur.fetchall()
        return render_template("feed.html", infoDetails=infoDetails)

@app.route('/feed-adm/')
def feed_adm():
    cur = mysql.connection.cursor()
    
    # Puxando informações do banco de dados.
    info = cur.execute("SELECT titulo, destinatario, data_inclusao, assunto, curso_id, mensagem FROM feed")

    if info > 0:
        infoDetails = cur.fetchall()
        return render_template("feed-adm.html", infoDetails=infoDetails)

@app.route('/envio-informacao/', methods=['GET','POST'])
def envio_informacao():
    # Solicitando informações da mensagem no formulário.
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_inclusao = request.form['data']
        assunto = request.form['assunto']
        curso = request.form['curso']
        destinatario = request.form['destinatario']
        mensagem = request.form['mensagem']
    # Inserindo informações na tabela feed.
        cursor = mysql.connection.cursor()
        cursor.execute("insert into feed(data_inclusao, assunto, destinatario, curso_id, titulo, mensagem) values (%s, %s, %s, %s, %s, %s)", (data_inclusao,assunto,destinatario,curso,titulo,mensagem))
        mysql.connection.commit()
    # Checando se as informações foram salvas.
        cursor.execute('select * from feed WHERE data_inclusao = %s and assunto = %s and curso_id = %s and titulo = %s and mensagem = %s and destinatario = %s', (data_inclusao,assunto,curso,titulo,mensagem,destinatario))
        status = cursor.fetchone()
        if status:
            return redirect(url_for('feed_adm'))
    return render_template('send-info.html')

if __name__ == '__main__':
    app.run()