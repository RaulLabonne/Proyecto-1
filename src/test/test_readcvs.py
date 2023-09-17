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

        weather_one = search("TLC")
        self.assertEqual(weathers_json[0], weather_one)

        weather_two = search("MTY")
        self.assertEqual(weathers_json[1], weather_two)

        cache["TLC"] = weather_one
        cache["MTY"] = weather_two

        self.assertDictEqual(getCache(self), cache)

    if __name__ == '__main__':
        unittest.main()
