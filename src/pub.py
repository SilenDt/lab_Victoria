class Pub:
    def __init__(self, name, till, list_of_drinks):
        self.name = name 
        self.till = till
        self.list_of_drinks = list_of_drinks

    def remove_drink(self, drink):
        self.list_of_drinks.remove(drink)
    
    def add_cash(self, amount):
        self.till += amount

    # def check_customer_of_drinking_age (self, age):
    #     if age >= 18:
    #         return True
    #     return False
