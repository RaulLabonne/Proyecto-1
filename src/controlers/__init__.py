from flask import Blueprint

resource = Blueprint('weather', __name__)

from . import controler
