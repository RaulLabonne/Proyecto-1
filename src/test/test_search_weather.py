import unittest
import requests
from dotenv import load_dotenv
import os

from src.models.search_weather import getCache
from src.models.search_weather import searchCache
from src.models.search_weather import request_iatacode
from src.models.search_weather import search

load_dotenv()

API_KEY = os.getenv("API_KEY") #La key para hacer llamadas a la api
class SearchWeather(unittest.TestCase):

    def test_read(self):
        invalid = 'Fail'
        try:
            search(invalid)
        except TypeError:
            """  """
        city = 'MEX'
        weather = search(city)
        iata = request_iatacode("MEX")  # Da un array de tama\~no 2, donde esta la latitud y longitud
        req = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(iata[0]) + '&lon=' + str(iata[1]) + '&appid=' + API_KEY)
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

    if __name__ == '__main__':
        unittest.main()
