# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from Burgers import Burger

class WesternBurger(Burger):
    '''
    This class represents a Western burger.
    It inherits from the Burger superclass and sets its specific name.
    '''

    def __init__(self):
        '''
        Initializes a new Western Burger.
        Calls the superclass constructor.
        '''
        super().__init__("Western Burger", 5.95)

    def get_name(self):
        '''
        Returns the name of this burger.
        @:returns string
        '''
        return "Delicious " + super().get_price() + " Burger"