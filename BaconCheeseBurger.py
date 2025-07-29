# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from Burgers import Burger

class BaconCheese(Burger):
    '''
    This class represents a Bacon Cheese burger.
    It inherits from the Burger superclass and sets its specific name.
    '''

    def __init__(self):
        '''
        Initializes a new Bacon Cheese Burger.
        Calls the superclass constructor.
        '''
        super().__init__("Bacon Cheese", 5.75)

    def get_name(self):
        '''
        Returns the name of this burger.
        @:returns string
        '''
        return "Delicious " + super().get_price() + " Burger"