from flask import render_template

from . import public


@public.route('/')
def index():
    return render_template("index.html")
