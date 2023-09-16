import unittest
import json

from src.models.readcvs import read
from src.models.search_weather import getCache
from src.models.search_weather import search


class ReadCVS(unittest.TestCase):

    def test_read(self):
        cache = {}
        self.assertDictEqual(getCache(self), cache)
        invalid = "error"
        try:
            read(invalid)
        except TypeError:
            """  """

        ticket = "kw9f0kwvZJmsukQy"
        weathers_json = read(ticket)

        test_weather_one = json.loads(weathers_json[0])
        weather_one = search("TLC")
        dict_one = json.loads(weather_one)
        self.assertDictEqual(test_weather_one, dict_one)

        test_weather_two = json.loads(weathers_json[1])
        weather_two = search("MTY")
        dict_two = json.loads(weather_two)
        self.assertDictEqual(test_weather_two, dict_two)

        cache["TLC"] = weather_one
        cache["MTY"] = weather_two

        self.assertDictEqual(getCache(self), cache)
