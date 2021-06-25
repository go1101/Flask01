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
    if user not in USERLIST: return False
    if USERLIST[user] != password: return False
    session['login'] = user
    return True


