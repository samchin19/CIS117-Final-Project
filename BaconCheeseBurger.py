# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from burgers import Burger

class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 5.75)