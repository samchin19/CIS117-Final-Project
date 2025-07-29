# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

class Burger:
    '''
    This class represents a generic burger with a name and a price.
    It serves as a superclass for specific menu items, providing
    basic attributes and methods for any type of burger.
    '''

    def __init__(self, name, price):
        '''
        Initializes a new Burger instance.
        '''
        self.name = name
        self.price = price

    def get_price(self):
        '''
        Returns the price of the burger.
        @:returns float
        '''
        return self.price

    def get_name(self):
        '''
        Returns the name of the burger.
        @:returns string
        '''
        return self.name