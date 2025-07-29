# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

'''
create customer as a superclass with an inheritable calculate tax method.
student tax is set to 0.
'''

# Constant for the tax
TAX_RATE = 0.09

class Customer:

    def __init__(self):
        pass

    def calculate_tax(self, subtotal):
        return subtotal * TAX_RATE