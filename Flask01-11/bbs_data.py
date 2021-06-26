import os, json, datetime

# [os.path.dirname(__file__)]でファイルのパスを取得する
BASE_DIR = os.path.dirname(__file__):
SAVE_FILE = BASE_DIR + '/data/log.json'

def load_data():
    # [log.json]ファイルの存在するか確認
    if not os.path.exists(SAVE_FILE):
        return []
    # jsonファイルを読み込みモード、文字コード[UTF-8]で開く
    with open(SAVE_FILE, 'rt', encoding='utf-8') as f:
        return json.load(f)
    
def save_data(data_list):
    # jsonファイルを書き込みモードで開き、引数[data_list]の内容を書き込む
    with open(SAVE_FILE, 'wt', encoding='utf-8') as f:
        json.dump(data_list, f)



