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

class DeAnzaBurger(Burger):
    def __init__(self):
        super().__init__("De Anza Burger", 5.25)

class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 5.75)

class MushroomSwiss(Burger):
    def __init__(self):
        super().__init__("Mushroom Swiss", 5.95)

class WesternBurger(Burger):
    def __init__(self):
        super().__init__("Western Burger", 5.95)

class DonCaliBurger(Burger):
    def __init__(self):
        super().__init__("Don Cali Burger", 5.95)
    
BURGER_CLASSES = [DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, DonCaliBurger]
