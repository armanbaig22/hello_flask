from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper():
        return f'<b>{fn()}</b>'
    return wrapper


def make_emphasis(fn):
    def wrapper():
        return f'<em>{fn()}</em>'
    return wrapper


def make_underlined(fn):
    def wrapper():
        return f'<u>{fn()}</u>'
    return wrapper


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route('/<name>')
def greet(name):
    return f"<p>Hi, {name}!</p>"


if __name__ == "__main__":
    app.run(debug=True)



