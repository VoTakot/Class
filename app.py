from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def slogan():
    return '<h1>И на Марсе будут яблони цвести!</h1>'

if __name__ == '__main__':
    app.run('127.0.0.1', 8080)