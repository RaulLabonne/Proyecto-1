import requests as rq
from os import getenv
from src.models.readdata import cityRow
from src.models.readdata import request_iatacode


__cache={}

def getCache(self):
    """Get the cache value.
    
    Returns
    -------
    dict
        the cache value
    """
    return __cache

def search(iata):
    """Search for weather information based on an IATA code.
    
     Parameters
    ----------
    iata :  str
        the IATA code of the city to search for.
        
    Returns
    -------
    json
        the weather information for the city.
    
    """
   
    row = cityRow(iata)
    key = row.loc[0,'IATA']
    nameCity = row.loc[0,'cities']
    coord = request_iatacode(row)
    weather = searchCache(key)
    if(weather==None):
       weather=request(coord,key) 
    weather['name'] = nameCity.upper()
    return weather

def request(coord, key):
    """Make a request to an API using the given coordinates and store the result in a cache with the given key.

    Parameters
    ----------
    coord : list
        the coordinates to use for the API request
    key : str
        the key to use for storing the result in the cache
        
    Returns
    -------
    json
        the weather data from the API response
    """
    weather=apiCall(coord,getenv("API_KEY"))
    __cache[key]=weather
    return weather


def apiCall(coord,key):
    """Make an API call to retrieve weather information based on the given coordinates.

     Parameters
    ----------
    coord : list
        a tuple containing the latitude and longitude coordinates
    key : str
        the API key
        
    Returns
    -------
    json
        the weather information in JSON format
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
    """Searches the cache for weather data associated with the given IATA code.

     Parameters
    ----------
    iata : str
        the IATA code for the location
        
    Returns
    -------
    json
        the weather data associated with the given IATA code, or None if not found in the cache.
    """
    weather=__cache.get(iata)
    return weather

def codeVerification(api):
    """Verify the status code of an API response and return an appropriate warning or error based on the code.
    
    Parameters
    ----------
    api : requests
        the API response object
        
    Returns
    -------
    error
        a warning or error type based on the status code
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