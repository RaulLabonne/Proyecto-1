from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html");

# @app.route('/search_ticket')
# def searchticket():
#     return render_template('search_ticket.html');

# @app.route('/search_city')
# def searchticket():
#     return render_template("search_city.html");

if __name__== "_main_" :
    app.run(debug = True, port=5000)
