from flask import render_template, request
from src.models.readcvs import read
from src.models.search_weather import search

from . import resource


@resource.route('/search_city', methods=['POST'])
def searchcity():
    """" Controller for search a city. If the length of city is 16, then city is a ticket and search the ticket.

    Returns
    -------
    str
        The render of result_city with all weather data of a city.
    """

    city = request.form['location']
    if len(city) == 16:
        return searchticket(city)
    weather_city = search(city)
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


@resource.errorhandler(404)
def page_not_found(fail):
    """Controller for errors that may occur during execution.

    Parameters
    ----------
    fail : str
        The error that happened.

    Returns
    -------
    str
        The render of 404.html with the error.
    """

    return render_template("404.html", errorS=fail), 404


def searchticket(ticket):
    """ Search the ticket and get the weather datas for their cities.

    Parameters
    ----------
    ticket : str
        The ticket to look for.

    Returns
    -------
    str
        The render of result_ticket with de data weather for their cities.
    """

    try:
        weathers_json = read(str(ticket))
        origin = weathers_json[0]
        destiny = weathers_json[1]
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
    """ Gets an array with the data weather of a city.

     Parameters
     ----------
     json : dict
        The Json that the API gave us of a city.

    Returns
    -------
    list
        All data weathers of a city.
    """
    
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
    """ Gives a message for a write error.

    Returns
    -------
    str
        The message that will show in 404.html.
    """

    return "lo la ciudad que buscas o ticket no estan en la base de datos"


def errorLectura():
    """ Gives a message for a read error.

    Returns
    -------
    str
        The message that will show in 404.html.
    """

    return "la base de datos no esta o contiene datos erroneos"


def errorAPI(num):
    """ Gives a message for an API error.

    If the number is 1, then the apy key is wrong write, in other case the error is of the server.

    Parameters
    ----------
    num : int, optional
        Type of error that happened

    Returns
    -------
    str
        The message that will show in 404.html
    """

    if (num == 1):
        return "tu API key no es valida, revisala"
    return "la API no responde, intente mas tarde"


def errorCall():
    """ Gives a message for a call error, this only occurs if the limit of API calls is exceeded

    Returns
    -------
    str
        The message that will show in 404.html.
    """
    return "se han superado el limite de llamadas permitidas, por favor espere un minuto o se baneara su API"
