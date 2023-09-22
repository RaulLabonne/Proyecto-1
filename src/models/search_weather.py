import requests as rq
from os import getenv
from src.database.readDB import dataCity
from src.models.levenstein import searchLev

API_KEY = getenv("API_KEY")

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
    weather=apiCall(coord)
    __cache[key]=weather
    return weather

def apiCall(coord):
    """
    Make an API call to retrieve weather information based on the given coordinates.
    @param coord: a tuple containing the latitude and longitude coordinates
    @return: the weather information in JSON format
    """
    url ='https://api.openweathermap.org/data/2.5/weather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&appid='+API_KEY
    api = rq.get(url)
    if(api.status_code!=200):
        return RuntimeError
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
        return TypeError
    cityData.reset_index(inplace=True, drop=False)
    return cityData