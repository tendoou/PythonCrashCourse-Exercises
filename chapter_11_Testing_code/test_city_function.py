import unittest
from City_function import get_full_city_name


class CitiesTest(unittest.TestCase):

    def test_city_country(self):
        new_city_name = get_full_city_name('santiago', 'chile')
        self.assertEqual(new_city_name, 'Santiago, Chile')

    def test_city_country_population(self):
        new_city_name = get_full_city_name('santiago', 'chile', '5000000')
        self.assertEqual(new_city_name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
