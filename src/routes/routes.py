from flask import render_template

from . import public


@public.route('/')
def index():
    """ Define the index of our page"""
    return render_template("index.html")
