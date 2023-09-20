import unittest
from src.models.levenstein import levenstein

class Levenstein(unittest.TestCase):
    
    def test_levenstein(self):
        cities = ['Monterrey','Mexico','Los Angeles']
        citiesBad = ['Montery','Mexic','Angeles']
        distanceTarget =[2,1,4] 
        result1 = levenstein(cities[0],citiesBad[0])
        result2 = levenstein(cities[1],citiesBad[1])
        result3 = levenstein(cities[2],citiesBad[2])
        self.assertEqual(distanceTarget[0],result1)
        self.assertEqual(distanceTarget[1],result2)
        self.assertEqual(distanceTarget[2],result3)
        
    if __name__ == '__main__':
        unittest.main()