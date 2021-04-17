from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    # テンプレートエンジンにデータを指定
    return render_template(
            'card-age.html',
            username='テスト太郎',
            age=25,
            email='test@example.com')
if __name__ == '__main__':
    app.run(debug=True)

