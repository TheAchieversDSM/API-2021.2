from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro/')
def cadastro():
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