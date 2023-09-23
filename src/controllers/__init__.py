from flask import Blueprint

weather_blueprint = Blueprint('weather_blueprint', __name__)

from . import processjson