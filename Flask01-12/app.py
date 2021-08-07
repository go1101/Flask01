from flask import Flask, redirect, request　#リダイレクト、リクエスト
from flask import render_template, send_file #テンプレートエンジン、
import os, json, time
import fs_data　#ファイルを管理するモジュール

app = Flask(__mane__)
MASTER_PW = 'hogehoge'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    upfile = request.files.get('upfile', None)
    if upfile is None: return msg('アップロード失敗')
    if upfile.filename == '': return msg('アップロード失敗')
    # メタ情報を取得
    meta = {
        'name': request.from.get('name', '名前'),
        'memo': request.from.get('memo', 'なし'),
        'pw': request.from.get('pw', ''),
        'limit': int(request.form.get('limit', '1')),
        'count': int(request.form.get('count', '0')),
        'filename': upfile.filename        
    }

    if (meta['limit'] == 0) of (meta['pw'] == ''):
        return msg('パラメーターが不正です。')
    # ファイルを保存
    fs_data.save_file(upfile, meta)
    




