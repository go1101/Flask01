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

@app.route('/check_login', methods=['POST'])
def check_login():
    # 空文字で初期化
    user, pw = (None, None)
    # フォームの値を代入
    if 'user' in request.form:
        user = request.form['user']
    if 'pw' in request.form:
        pw = request.form['pw']
    # ユーザー名かパスワードが空文字のままならトップページへリダイレクトする
    if (user is None) or (pw is None):
        return redirect('/')
    
    # ログインチェック（try_login関数は後半で定義）
    if try_login(user, pw) == False:
        return """
        <h1>ユーザー名かパスワードに誤りがあります。</h1>
        <p><a href="/">戻る</a></p>
        """
    # ログイン情報が正しければ非公開ページへ
    return redirect('private')

@app.route('/private')
def private_page():
    # ログインしていなければトップに戻す（is_login関数は後半で定義）
    if not is_login():
        return """
        <h1>ログインして下さい。</h1>
        <p><a href="/">ログインする</a></p>
        """
    
    return """
    <h1>非公開ページです。</h1>
    <p>ログイン中です。</p>
    <p><a href="/logout">ログアウト</a></p>
    """

@app.route('/logout')
def logout_page():
    try_logout()
    return """
    <h1>ログアウトしました。</h1>
    <p><a href="/">戻る</a></p>
    """


def is_login():
    if 'login' in session:
        return True
    return False

def try_login(user, password):
    if not user in USERLIST:
        return False
    if USERLIST[user] != password:
        return False
    session['login'] = user
    return True

def try_logout():
    session.pop('login', None)
    return True

if __name__ == '__main__':
    app.run(debug=True)



