from flask import Flask, render_template, session, request, redirect, url_for
import os
import wikipedia

# pref_question.pyファイルよりpref_location関数をインポートする
from pref_question import pref_location
from wiki import wiki

# インスタンスの作成
app = Flask(__name__)

# セッション情報を暗号化するために、暗号鍵を作成する
# urandom()関数により10桁の乱数を生成する
key = os.urandom(10)
app.secret_key = key

# ユーザID[lelouch]とパスワード[vermillion]を辞書型で作成
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

@app.route('/logout')
def logout():
    return render_template('login.html')

# ログイン認証、POSTメソッドにより情報を受取る
@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']
    # 取得したユーザIDとパスワードが[id_pwd]に含まれるかをifで判断する

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


# [index.html]のformより[/pref_quiz]へアクセスした時の動作
@app.route('/pref_quiz', methods=['POST'])
def pref_quiz():
    # [pref_question.py]のpref_location()関数を実行
    # pref_location()関数の戻り値を各変数に代入
    # 各変数をセッションごとの変数に代入
    random_pref, city_name, pref_url = pref_location()
    session['prefecture'] = random_pref
    session['city'] = city_name
    session['url'] = pref_url
    return render_template('quiz.html',prefecture=random_pref)
    

@app.route('/answercheck', methods=['POST'])
def answercheck():
    user_answer = request.form['city']
    prefecture = session.get('prefecture')
    city = session.get('city')
    url = session.get('url')

    if user_answer == city:
        result = '正解'
    else:
        result = '不正解'
    return render_template('result.html', result=result, prefecture=prefecture, city=city, url=url)

@app.route('/wikipedia', methods=['POST'])
def wikipedia():
    return render_template('wiki_result.html', result='検索文字を入力下さい')

# [wiki_result.html]より入力した情報を引数として[wiki_result.html]へ渡す
@app.route('/wiki_answer', methods=['POST'])
def wiki_answer():
    word = request.form['word']
    if word == '':
        result = '検索情報を入力して下さい。'
    else:
        result = wiki(word)
    
    return render_template('wiki_result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

