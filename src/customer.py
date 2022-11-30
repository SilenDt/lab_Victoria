class Customer:
    def __init__(self, name, wallet, age):
        self.name = name 
        self.wallet = wallet
        self.age = age

    def remove_cash(self, amount):
        self.wallet -= amount

    def customer_age (self):
        return self.age

    
