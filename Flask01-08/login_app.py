from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = 'hogehoge'

USERLIST = {
    'username01': 'password01',
    'username02': 'password02',
}

@app.route('/')
def index():
    return """
    <html><body><h1>ログインフォーム</h1>
    <form action="/check_login" method="POST">
    ユーザー名：<br>
    <input type="text" name="user"><br>
    パスワード：<br>
    <input type="password" name="pw"><br>
    <input type="submit" value="ログイン">
    </form>
    <p><a href="/private">秘密鍵</a></p>
    """

