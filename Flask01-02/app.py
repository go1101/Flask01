from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # データを指定
    username = 'ケンジ'
    age = 19
    email = 'kenji@example.com'

    # テンプレートエンジンにデータを指定
    return render_template('card.html',
            username=username,
            age=age,
            email=email)

if __name__ == '__main__':
    app.run(debug=True)

