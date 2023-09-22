from flask import request, render_template
from src.models.readcvs import read
from src.models.search_weather import search
from . import weather_blueprint


@weather_blueprint.route('\result_ticket', methods=['POST'])
def searchticket():
    ticket = request.form['search_ticket']
    weathers_json = read(str(ticket))
    origin = weathers_json[0]
    origin_weather = toString(origin)
    destiny = weathers_json[1]
    destiny_weather = toString(destiny)
    return render_template('result_city.html',
                           city_Arrival=origin_weather[0],
                           weather_arrival=origin_weather[1],
                           temp_arrival=origin_weather[2],
                           temp_min_arrival=origin_weather[3],
                           temp_max_arrival=origin_weather[4],
                           sensation_arrival=origin_weather[5],
                           humidity_arrival=origin_weather[6],
                           pressure_arrival=origin_weather[7],
                           speed_arrival=origin_weather[8],
                           precipitation_arrival=origin_weather[9],
                           city_destiny=destiny_weather[0],
                           weather_destiny=destiny_weather[1],
                           temp_destiny=destiny_weather[2],
                           temp_min_destiny=destiny_weather[3],
                           temp_max_destiny=destiny_weather[4],
                           sensation_destiny=destiny_weather[5],
                           humidity_destiny=destiny_weather[6],
                           pressure_destiny=destiny_weather[7],
                           speed_destiny=destiny_weather[8],
                           precipitation_destiny=destiny_weather[9]
                           )


@weather_blueprint.route('\result_city', methods=['GET'])
def searchcity():
    city = request.args.get('search_city')
    weather_city = search(str(city))
    data_weather = toString(weather_city)
    return render_template('result_city.html',
                           city=data_weather[0],
                           weather_type=data_weather[1],
                           temp=data_weather[2],
                           min_temp=data_weather[3],
                           max_temp=data_weather[4],
                           sensation=data_weather[5],
                           humidity=data_weather[6],
                           pressure=data_weather[7],
                           speed=data_weather[8],
                           precipitation=data_weather[9]
                           )
    """"

"""


def toString(json):
    dict_weather = json['weather']
    city = json['name']
    list_weather = dict_weather[0]
    weather_type = list_weather['main']
    main = json['main']
    temp = main['temp']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    sensation = main['feels_like']
    humidity = main['humidity']
    pressure = main['pressure']
    wind_dic = dict_weather['wind']
    speed = wind_dic['speed']
    rain_dict = dict_weather['rain']
    rain = rain_dict['1h']
    return [city, weather_type, temp, temp_min, temp_max, sensation, humidity, pressure, speed, rain]
