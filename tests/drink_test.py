import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.instance_of_drink = Drink("Martini", 10.00)

    def test_drink_has_name(self):
        self.assertEqual("Martini", self.instance_of_drink.name)

    def test_drink_has_price(self):
        self.assertEqual(10.00, self.instance_of_drink.price)