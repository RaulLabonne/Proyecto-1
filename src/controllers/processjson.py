from flask import Blueprint, request
from src.models.readcvs import read
from src.models.search_weather import search
import json

weather_blueprint = Blueprint('weather_blueprint', __name__)


@weather_blueprint.route('\search_ticket', methods=['POST'])
def searchticket():
    ticket = request.form['search_ticket']
    weathers_json = read(str(ticket))

@weather_blueprint.route('\search_city', methods=['GET'])
def searchcity():
    city = request.args.get('search_city')
    weather_city = search(str(city))
    dict_city = json.load(weather_city)


    """"

"""
def toString(dict):
    dict_weather = dict['weather']