# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
from Customer import Customer


class Student(Customer):
    def calculate_tax(self, subtotal):
        return 0.0