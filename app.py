from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',methods=('GET','POST'))
def index():
    if request.method=="POST":
        cadena = request.form.get("location")
        print(cadena)
    else:
        return render_template("index.html/");

@app.route('/search_ticket')
def searchticket():
    return 'Searching ticket';

@app.route('/search_city')
def searchcity():
    return 'Searching city';

# @app.route('/result_city')
# def result():
#     return render_template("result_city.html");

def page_not_found(error):
    return render_template("page_not_found.html"),404

if __name__== "_main_" :
    app.register_error_handler(404, page_not_found)
    app.run(debug = True, port=5000)
