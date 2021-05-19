from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの作成
app = Flask(__name__)

# 暗号鍵の作成
key = os.urandom(10)
app.secret_key = key

# ユーザIDとパスワードを辞書型で作成
id_pwd = {'lelouch':'vermillion'}

@app.route('/')
def index():
    return "hell world"

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

