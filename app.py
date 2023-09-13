from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template("base.html");

if __name__== "_main_" :
    app.run(debug = True)
