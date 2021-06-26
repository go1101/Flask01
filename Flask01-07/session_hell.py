from flask import Flask, request, session, redirect
app = Flask(__name__)
# セッション情報を暗号化するためのキー、任意の文字列で問題無い
app.secret_key = 'hogehoge'

@app.route('/')
def index():
    # 入力フォーム、GETメソッドで[username]を取得する
    return """
    <html><body><h1>ユーザー名</h1>
    <form action="/setname" method="GET">
        名前：<input type="text" name="username">
        <input type='submit' value='開始'>
    </form></body></html>
    """

# 入力フォームから取得した[username]をもとに処理、未入力の場合はトップページにリダイレクト
@app.route('/setname')
def setname():
    name = request.args.get('username')
    if not name: return redirect('/')
    # セッションにフォームで入力された[username]を代入する
    session['name'] = name
    return redirect('/morning')

def getLinks():
    return """
    <ul>
    <li><a href="/morning">朝の挨拶</a></li>
    <li><a href="/hello">昼の挨拶</a></li>
    <li><a href="/night">夜の挨拶</a></li>
    </ul>
    """

@app.route('/morning')
def morning():
    # セッション情報(session['name'])が存在しなければホーム画面へリダイレクト
    if not ('name' in session):
        return redirect('/')
    # セッション情報を変数[name]に代入
    # 上記で定義している[getLinks]関数を実行する
    name = session['name']
    return """
    <h1>{0}さん、おはようございます。</h1>{1}
    """.format(name ,getLinks())


@app.route('/hello')
def hello():
    if not ('name' in session):
        return redirect('/')
    name = session['name']
    return """
    <h1>{0}さん、こんにちは。</h1>{1}
    """.format(name ,getLinks())

@app.route('/night')
def night():
    if not ('name' in session):
        return redirect('/')
    name = session['name']
    return """
    <h1>{0}さん、こんばんは。</h1>{1}
    """.format(name ,getLinks())



if __name__ == '__main__':
    app.run(debug=True)


