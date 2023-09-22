import unittest
import requests
from dotenv import load_dotenv
import os
from src.database.readDB import dataCity
from src.models.search_weather import getCache
from src.models.search_weather import searchCache
from src.models.search_weather import request_iatacode
from src.models.search_weather import search
from src.models.search_weather import apiCall
load_dotenv()
API_KEY = os.getenv("API_KEY") #La key para hacer llamadas a la api

class SearchWeather(unittest.TestCase):
    maxDiff = 1974
    def test_search(self):
        invalid = 'Fail'
        try:
            search(invalid)
        except TypeError:
            """  """
        data = dataCity()
        city = data[data['IATA']=="MEX"]
        city.reset_index(inplace=True, drop=False)
        weather = search('MEX')
        iata = request_iatacode(city)  # Da un array de tama\~no 2, donde esta la latitud y longitud
        req = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(iata[0]) + '&lon=' + str(iata[1]) + '&appid=' + os.getenv("API_KEY")+'&units=metric')
        compare_json = req.json()
        self.assertEqual(weather, compare_json)

    def test_cache(self):
        cache = {}
        self.assertDictEqual(cache, getCache(self))
        city = 'MTY'
        weather = search(city)
        self.assertFalse(getCache(self) == cache)
        cache['MTY'] = weather
        self.assertDictEqual(getCache(self), cache)
        compare_json = searchCache('MTY')
        self.assertEqual(weather, compare_json)
    
    def test_codes(self):
        print("aqui empieza 3")
        badAPI="dontwork"
        badcoords=[3000, 250]
        goodcoords=[51.5085,-0.1257]
        test = True
        try:
            apiCall(goodcoords,badAPI)
            test = False
        except ValueError:
            test = True
        try:
            apiCall(badcoords,os.getenv("API_KEY"))
            test = False
        except SyntaxError:
            test = True 
        print(test)
        self.assertTrue(test)
        
        

    if __name__ == '__main__':
        unittest.main()
    

