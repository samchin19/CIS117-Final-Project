# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

TAX_RATE = 0.09

class Customer:
    def__init__(self):
        pass
    def calculate_tax(self, subtotal):
        return subtotal * TAX_RATE

class Student(Customer):
    def calculate_tax(self, subtotal):
        return 0.0

class RegularCustomer(Customer):
    pass
