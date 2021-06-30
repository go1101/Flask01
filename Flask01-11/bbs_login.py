from flask import session, redirect

# 辞書型の変数[USERLIST]を定義
USERLIST = {
    'test01': 'TEST01',
    'test02': 'TEST02',
    'test03': 'TEST03',
}

def is_login():
    # セッション情報(session['login'])の情報を元に、True or Falseを返す
    return 'login' in session

# ログイン確認
def try_login(user, password):
    # 引数[user]が辞書型の変数[USERLISK]のキーに存在するか確認
    if user not in USERLIST: return False
    # 引数[user]に紐づく値が、引数[password]と一致するか確認
    if USERLIST[user] != password: return False
    session['login'] = user
    return True

def try_logout():
    # セッション情報(session['login'])を削除(初期化する)
    session.pop('login', None)
    return True

def get_user():
    # 上記で定義した[is_login]関数でセッション情報が取得できれば、セッション情報を返す
    # セッション情報が存在しなければ'not login'を返す
    if is_login(): return session['login']
    return 'not login'
    

