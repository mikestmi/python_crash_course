import unittest
from city_functions import get_formatted_city_name

class CityNamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country_name(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        formatted_name = get_formatted_city_name('santiago', 'chile', '5000000')

if __name__ == '__main__':
    unittest.main()
