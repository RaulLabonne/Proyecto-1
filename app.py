from flask import Flask, render_template, request, redirect, url_for
from src.models.readcvs import read
from src.models.search_weather import search
from werkzeug.exceptions import HTTPException
import pprint

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        cadena = request.form.get("location")
    else:
        return render_template("index.html/")


@app.route('/search_city', methods=['POST'])
def searchcity():
    city = request.form['location']
    if len(city) == 16:
        return searchticket(city)
    try:
        weather_city = search(city)
    except TypeError:
        return page_not_found(errorEscritura())
    except ValueError:
        return page_not_found(errorAPI(1))
    except SyntaxError:
        return page_not_found(errorLectura())
    except UserWarning:
        return page_not_found(errorCall())
    except FutureWarning:
        return page_not_found(errorAPI())
    
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
                           clouds=data_weather[9],
                           )


def searchticket(ticket):
    
    weathers_json = read(str(ticket))
    try:
        origin = weathers_json[0]
    except TypeError:
        return page_not_found(errorEscritura())
    except ValueError:
        return page_not_found(errorAPI(1))
    except SyntaxError:
        return page_not_found(errorLectura())
    except UserWarning:
        return page_not_found(errorCall())
    except FutureWarning:
        return page_not_found(errorAPI())
    
    origin_weather = toString(origin)
    try:
        destiny = weathers_json[1]
    except TypeError:
        return page_not_found(str(errorEscritura()))
    except ValueError:
        return page_not_found(errorAPI(1))
    except SyntaxError:
        return page_not_found(errorLectura())
    except UserWarning:
        return page_not_found(errorCall())
    except FutureWarning:
        return page_not_found(errorAPI())
    
    destiny_weather = toString(destiny)
    return render_template('result_ticket.html',
                           ticket_html=ticket,
                           city_arrival=origin_weather[0],
                           weather_arrival=origin_weather[1],
                           temp_arrival=origin_weather[2],
                           temp_min_arrival=origin_weather[3],
                           temp_max_arrival=origin_weather[4],
                           sensation_arrival=origin_weather[5],
                           humidity_arrival=origin_weather[6],
                           pressure_arrival=origin_weather[7],
                           speed_arrival=origin_weather[8],
                           clouds_arrival=origin_weather[9],
                           city_destiny=destiny_weather[0],
                           weather_destiny=destiny_weather[1],
                           temp_destiny=destiny_weather[2],
                           temp_min_destiny=destiny_weather[3],
                           temp_max_destiny=destiny_weather[4],
                           sensation_destiny=destiny_weather[5],
                           humidity_destiny=destiny_weather[6],
                           pressure_destiny=destiny_weather[7],
                           speed_destiny=destiny_weather[8],
                           clouds_destiny=destiny_weather[9]
                           )


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
    wind_dic = json['wind']
    speed = wind_dic['speed']
    clouds_dict = json['clouds']
    clouds = clouds_dict['all']
    return [city, weather_type, temp, temp_min, temp_max, sensation, humidity, pressure, speed, clouds]


def errorEscritura():
    return "lo la ciudad que buscas o ticket no estan en la base de datos"
def errorLectura():
    return "la base de datos no esta o contiene datos erroneos"
def errorAPI(num):
    if(num==1):
        return "tu API key no es valida, revisala"
    return "la API no responde, intente mas tarde"
def errorCall():
    return "se han superado el limite de llamadas permitidas, por favor espere un minuto o se baneara su API"

@app.errorhandler(404)
def page_not_found(fail):
    return render_template("404.html",errorS=fail), 404


if __name__ == "_main_":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)
