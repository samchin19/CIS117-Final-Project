# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

'''
create customer as a superclass with an inheritable calculate tax method.
student tax is set to 0.
'''

# Constant for the tax
TAX_RATE = 0.09

class Customer:
    '''
    This class represents any user that interacts with the program.
    It serves as a superclass, providing a base method for calculating tax
    on a subtotal.
    '''

    def __init__(self):
        '''
        Initializes a new Customer instance.


        '''
        pass

    def calculate_tax(self, subtotal):
        '''
        Calculates the tax amount for a given subtotal.
        :param subtotal:
        :return:
        '''
        return subtotal * TAX_RATE