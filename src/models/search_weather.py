import requests as rq
import os
from dotenv import load_dotenv
from src.database.readDB import dataCity
from src.models.levenstein import searchLev
load_dotenv()
API_KEY = os.getenv("API_KEY")

__cache={}

def getCache(self):
    return __cache

def search(iata):
    row = cityRow(iata)
    key = row.loc[0,'IATA']
    coord = request_iatacode(row)
    weather = searchCache(key)
    if(weather==None):
       weather=request(coord,key) 
    return weather

def request(coord, key):
    weather=apiCall(coord)
    __cache[key]=weather
    return weather

def apiCall(coord):
    url ='https://api.openweathermap.org/data/2.5/weather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&appid='+API_KEY
    api = rq.get(url)
    if(api.status_code!=200):
        print('error')
        return RuntimeError
    return api.json()

def searchCache(iata):
    weather=__cache.get(iata)
    return weather


def request_iatacode(cityData):
    coord=[cityData.loc[0,'latitude'],cityData.loc[0,'longitude']]
    return coord

def cityRow(code):
    cityData =searchLev(code)
    if(cityData.empty):
        return TypeError
    cityData.reset_index(inplace=True, drop=False)
    return cityData