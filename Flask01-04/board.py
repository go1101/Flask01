# Flaskをインポート
# request、入力した内容を受け取る

from flask import Flask, request, redirect
import os
app = Flask(__name__)

# データ保存先のテキストを指定、入力した内容が下記のテキストに保存される
DATAFILE = './board-data.txt'

@app.route('/')
def index():
    msg = 'まだ書き込みはありません。'
    # テキストの内容を確認する、文章があれば、変数msgを上書きする
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()
            # ダブルコーテーション3つで直下のHTMLの内容を表示する
            # POSTメソッドで入力した内容を書き込む
        return """
<html><body>
<h1>メッセージボード</h1>
<div style="background-color:yellow;padding:3em;">
{0}</div>
<h3>ボードの内容を更新：</h3>
<form action="/write" method="POST">
    <textarea name="msg"
    rows="6" cols="60"></textarea><br/>
    <input type="submit" value=" 書込 ">
</form>
</body></html>
""".format(msg)

#POSTメソットにより受け取っと入力結果を、'/'にリダイレクトする
@app.route('/write' ,methods=['POST'])
def write():
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
    return redirect('/')

if __name__ == '__main__':
    # デバッグモードで実行、ソースコード更新で自動リロード
    app.run(debug=True)

