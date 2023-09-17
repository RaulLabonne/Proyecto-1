import requests as rq
import pandas as pd
import os
from dotenv import load_dotenv
from src.database.readDB import dataDB, dataCity
load_dotenv()
API_KEY = os.getenv("API_KEY") 
cache = {}

def getCache(self):
    return cache


def search(iata):
    data = dataCity()
    coord = request_iatacode(iata)
    weather = searchCache(iata)
    if(weather==None):
        weather=apiCall(coord)
        cache[iata]=weather

    return weather

def apiCall(coord):
    url ='https://api.openweathermap.org/data/2.5/weather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&appid='+API_KEY
    api = rq.get(url)
    if(api.status_code!=200):
        print('error')
        return RuntimeError
    return api.json()

def searchCache(iata):
    weather=cache.get(iata)
    return weather


def request_iatacode(code):
    data = dataCity()
    cityData = data[data['IATA']==code]
    if(cityData.empty):
        return TypeError
    cityData.reset_index(inplace=True, drop=False)
    coord=[cityData.loc[0,'latitude'],cityData.loc[0,'longitude']]
    return coord
