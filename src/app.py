from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '(Insira sua senha...)'
app.config['MYSQL_DB'] = 'api_fatec'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['e-mail']
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute('select * from usuario WHERE email = %s and senha = %s', (email,senha))
        conta = cursor.fetchone()
        if conta:
            return redirect(url_for('feed'))
    return render_template('login.html')

@app.route('/cadastro/',methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['e-mail']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute("insert into usuario(email,senha,nome) values (%s, %s,%s)", (email,senha,nome))
        mysql.connection.commit()
        cursor.execute('select * from usuario WHERE email = %s and senha = %s ', (email,senha))
        status = cursor.fetchone()
        if status:
            return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/feed/')
def feed():
    return render_template('feed.html')

@app.route('/feed-adm/')
def feed_adm():
    return render_template('feed-adm.html')

@app.route('/envio-informacao/')
def envio_informacao():
    return render_template('send-info.html')

if __name__ == '__main__':
    app.run()
