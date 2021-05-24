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
    if not session.get('login'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# ログイン認証、POSTメソッドにより情報を受取る
@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        session['login'] = False
    
    # 認証が成功したらindex()関数を実行、失敗したらlogin()関数を実行する
    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)

