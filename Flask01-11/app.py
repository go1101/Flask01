from flask import Flask, redirect, url_for, session
from flask import render_template, request
import os, json, datetime
import bbs_login
import bbs_data

# Flaskのインスタンスを生成
app.= Flask(__name__)
app.secret_key = 'hogehoge'

@app.route('/')
def index():
    # [bss_login.py]の[is_login()]関数より、セッション情報を保有しているかをTrue or Falseで評価する
    # セッション情報が無ければ(ログインしていなければ)ログイン画面へ遷移
    if not bbs_login.is_login():
        return redirect('/login')
    # セッション情報があれば、ユーザー名と日時情報を[index.html]へ渡し、表示する
    return render_template('index.html', user=bbs_login.get_user(), data=bbs_data.load())

# セッション情報が無ければログイン画面へ遷移する
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/try_login' methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')

    # [bss_login.py]の[try_login]関数に[user]と[pw]を引数として渡し、[URSELIST]の情報と一致するか評価する
    if bss_login.try_login(user, pw):
        # ログイン認証ができると、セッション情報([)session['login'])に[user]情報を渡し、トップ画面に遷移する
        return redirect('/')
    # 認証情報が一致しなければ、エラーメッセージを[show_msg]関数(msg.html)に渡して、表示する
    return show_msg('ログインに失敗しました。')

@app.route('/logout')
def logout():
    bss_login.try_logout()
    return show_msg('ログアウトしました。')

# 書込処理
@app.route('/write', methods=['POST'])
def write():
    # ログイン情報(session['login'])の有無を評価する
    if not bbs_login.is_login():
        # ログイン情報が無ければ、ログイン画面へ遷移する
        return redirect('/login')
    # [/write]フォームより書込情報を取得、無ければ['']を取得
    ta = request.form.get('ta','')
    # [/write]フォームの書込情報が無ければエラーメッセージを表示
    if ta = '': return show_msg('書き込みが空でした')
    # 書き込みがあればユーザ名と書き込み情報を引数にして、[bbs_data.py]の[save_data_append]関数を実行する
    bss_data.save_data_append(user=bbs_login.get_user(), text=ta)
    return redirect('/')

def show_msg(msg):
    return render_template('msg.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)


    

