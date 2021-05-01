from flask import Flask
from flask import render_template

app: Flask = Flask(__name__)

SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def hello_world():
    return render_template("splash.html")

@app.route('/main')
def maincandy():
    return render_template("candymain.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/why')
def why():
    return render_template("why.html")

@app.route('/creditcard')
def creditcard():
    return render_template("carddata.html")

@app.route('/comp')
def comp():
    return render_template("comp.html")


if __name__ == '__main__':
    app.run("0.0.0.0",5000)
