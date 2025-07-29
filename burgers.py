# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

'''
creates Burger as a superclass and the specific menu items as subclasses of burgers with name and pricing
'''
class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name