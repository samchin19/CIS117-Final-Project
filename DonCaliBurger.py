# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from Burgers import Burger

class DonCaliBurger(Burger):
    '''
    This class represents a Don Cali burger.
    It inherits from the Burger superclass and sets its specific name.
    '''
    def __init__(self):
        '''
        Initializes a new Don Cali Burger.
        Calls the superclass constructor.
        '''
        super().__init__("Don Cali Burger", 5.95)

    def get_name(self):
        '''
        Returns the name of this burger.
        @:returns string
        '''
        return "Delicious " + super().get_price() + " Burger"