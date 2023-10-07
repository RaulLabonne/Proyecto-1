from flask import render_template

from . import public


@public.route('/')
def index():
    return render_template("index.html")


@public.errorhandler(404)
def page_not_found():
    return render_template("page_not_found.html"), 404
