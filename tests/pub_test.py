import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.instance_of_drink1 = Drink("Beer", 7.00)
        self.instance_of_drink2 = Drink("Wine", 6.00)
        self.instance_of_drink3 = Drink("Martini", 10.00)
        self.instance_of_drink4 = Drink("Vodka", 4.00)
        list_of_drinks = [self.instance_of_drink1,self.instance_of_drink2, self.instance_of_drink3,self.instance_of_drink4]
        self.instance_of_pub = Pub("The Chanter", 1000.00, list_of_drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.instance_of_pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000.00, self.instance_of_pub.till)

    def test_remove_drink(self):
        self.instance_of_pub.remove_drink(self.instance_of_drink1)
        self.assertEqual(3, len(self.instance_of_pub.list_of_drinks))

    
    def test_add_cash_to_till(self):
        self.instance_of_pub.add_cash(7)
        self.assertEqual(1007.00, self.instance_of_pub.till)

    def test_pub_can_sell_drink(self):
        self.instance_of_customer = Customer('Jane', 200.00, 20)
        self.instance_of_pub.remove_drink(self.instance_of_drink1)
        self.instance_of_pub.add_cash(7)
        self.instance_of_customer.remove_cash(7)

        self.assertEqual(3, len(self.instance_of_pub.list_of_drinks))
        self.assertEqual(1007.00, self.instance_of_pub.till)
        self.assertEqual(193.00, self.instance_of_customer.wallet)

    def test_customer_of_drinking_age(self):
        # self.check_customer_of_drinking_age >= 18
        self.assertEqual(True, self.check_customer_of_drinking_age(20))


    