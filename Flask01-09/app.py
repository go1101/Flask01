from flask import Flask, request, redirect
from datetime import datetime
import os

IMAGES_DIR = './static/images'
IMAGES_URL = '/static/images'
app = Flask(__name__)

@app.route('/')
def index_page():
    return """
    <html><body><h1>アップロード</h1>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="upfile">
        <input type="submit" value="アップロード">
    </form>
    </body></html>
    """

@app.route('upload')
def upload():
    if not (upfile in request.files):
        return redirect('/')
    temp_file = request.files['upfile']
    