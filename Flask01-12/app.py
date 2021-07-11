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
    

