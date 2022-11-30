import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.instance_of_customer = Customer("Jane", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Jane", self.instance_of_customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(200.00, self.instance_of_customer.wallet)

    def test_customer_can_remove_cash(self):
        self.instance_of_customer.remove_cash(7)
        self.assertEqual(193.00, self.instance_of_customer.wallet)

    # def test_customer_buy_drink(self):
        