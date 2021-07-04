import os, json, datetime

# [os.path.dirname(__file__)]でファイルのパスを取得する
BASE_DIR = os.path.dirname(__file__)
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
        json.dump(data_list, f, indent=2, ensure_ascii=False)

# [index.html]の書き込みボタンが押されると、[save_data_append]関数が実行される
def save_data_append(user, text):
    # [get_datetime_now]関数により現在日付を取得
    tm = get_datetime_now()
    data = {'name': user, 'text': text, 'date': tm}
    # [load_data]関数よりjsonファイルを読み込みモードで開き、data_list変数に代入
    data_list = load_data()
    # data_listの先頭にdata変数の情報を記載する
    data_list.insert(0, data)
    # [save_data]関数によりdata_listの内容をjsonファイルに書き込む
    save_data(data_list)

def get_datetime_now():
    now = datetime.datetime.now()
    return "{0:%Y%m%d %H:%M}".format(now)


