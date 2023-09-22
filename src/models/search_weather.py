import requests as rq
from os import getenv
from src.database.readDB import dataCity
from src.models.levenstein import searchLev



__cache={}

def getCache(self):
    """
    Get the cache value.
    @return: the cache value
    """
    return __cache

def search(iata):
    """
    Search for weather information based on an IATA code.
    @param iata: the IATA code of the city to search for.
    @return: the weather information for the city.
    """
    row = cityRow(iata)
    key = row.loc[0,'IATA']
    coord = request_iatacode(row)
    weather = searchCache(key)
    if(weather==None):
       weather=request(coord,key) 
    return weather

def request(coord, key):
    """
    Make a request to an API using the given coordinates and store the result in a cache with the given key.
    @param coord: the coordinates to use for the API request
    @param key: the key to use for storing the result in the cache
    @return: the weather data from the API response
    """
    weather=apiCall(coord,getenv("API_KEY"))
    __cache[key]=weather
    return weather


def apiCall(coord,key):
    """
    Make an API call to retrieve weather information based on the given coordinates.
    @param coord: a tuple containing the latitude and longitude coordinates
    @return: the weather information in JSON format
    """
    url ='https://api.openweathermap.org/data/2.5/weather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&appid='+key+'&units=metric'
    api = rq.get(url)
    try:
        codeVerification(api)
    except ValueError:
        raise ValueError
    except SyntaxError:
        raise SyntaxError
    except UserWarning:
        raise UserWarning
    except FutureWarning:
        raise FutureWarning
    return api.json()

def searchCache(iata):
    """
    Searches the cache for weather data associated with the given IATA code.
    @param iata: the IATA code for the location
    @return: the weather data associated with the given IATA code, or None if not found in the cache.
    """
    weather=__cache.get(iata)
    return weather


def request_iatacode(cityData):
    """
    Given city data, extract the latitude and longitude coordinates of the city.
    @param cityData: the dataFrame containing latitude and longitude information
    @return: the latitude and longitude coordinates of the city
    """
    coord=[cityData.loc[0,'latitude'],cityData.loc[0,'longitude']]
    return coord

def cityRow(code):
    """
    Given a city code, retrieve the corresponding city data from a search function.
    @param code: the city code
    @return: the city data as a pandas DataFrame. If no data is found, return a TypeError.
    """
    if(len(code)>3):
        cityData =searchLev(code)
    else:
        data = dataCity()
        cityData = data[data["IATA"]==code]
    if(cityData.empty):
        raise TypeError
    cityData.reset_index(inplace=True, drop=False)
    return cityData

def codeVerification(api):
    """
    Verify the status code of an API response and return an appropriate warning or error based on the code.
    @param api: the API response object
    @return: a warning or error type based on the status code
    """
    if(api.status_code == 401): #this is a API key error
        raise ValueError
    if(api.status_code == 400): #this is a this is an error in the coordinates
        raise SyntaxError
    if(api.status_code == 429): #this is an error in the maximum requests
        raise UserWarning
    if(api.status_code >= 500): #this is a server error
        raise FutureWarning
    return ""