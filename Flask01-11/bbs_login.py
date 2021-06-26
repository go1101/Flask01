from flask import session, redirect

USERLIST = {
    'test01': 'TEST01'
    'test02': 'TEST02'
    'test03': 'TEST03'
}

def is_login():
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
    session.pop('login', None)
    return True

def get_user():
    if is_login(): return session['login']
    return 'not login'
    

