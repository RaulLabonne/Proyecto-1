import unittest

from src.models.readcvs import read
import src.models.search_weather  as sw



class ReadCVS(unittest.TestCase):

    def test_read(self):
        cache = {}
        self.assertDictEqual(sw.getCache(self), cache)
        invalid = "error"
        try:
            read(invalid)
        except TypeError:
            """ """
        ticket = "kw9f0kwvZJmsukQy"
        weathers_json = read(ticket)

        weather_one = sw.search("TLC")
        self.assertEqual(weathers_json[0], weather_one)
        
        weather_two =sw.search("Monterrey")
        self.assertEqual(weathers_json[1], weather_two)
        cache["TLC"] = weather_one
        cache["MTY"] = weather_two
        
        self.assertDictEqual(sw.getCache(self), cache)

    if __name__ == '__main__':
        unittest.main()
