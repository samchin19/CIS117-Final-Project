# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from Burgers import Burger

class MushroomSwiss(Burger):
    '''
    This class represents a Mushroom Swiss burger.
    It inherits from the Burger superclass and sets its specific name.
    '''
    def __init__(self):
        '''
        Initializes a new Mushroom Swiss Burger.
        Calls the superclass constructor.
        '''
        super().__init__("Mushroom Swiss", 5.95)

    def get_name(self):
        '''
        Returns the name of this burger.
        @:returns string
        '''
        return "Delicious " + super().get_price() + " Burger"