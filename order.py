# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

from burgers import BURGER_CLASSES
from customer import Student, RegularCustomer

class Order:
    def __init__(self):
        self.items = []
        
    def add_item(self, burger, quantity):
        self.items.append((burger, quantity))
        
    def calc_total(self, customer):
        subtotal = sum(burger.get_price() * quantity for burger, quantity in self.items)
        tax = customer.calculate_tax(subtotal)
        total = subtotal +tax
        return subtotal, tax, total

    def print_bill(self, subtotal, tax, total):
        print("\nYour Bill:")
        print("*" * 50)
        
        for burger, quantity in self.items:
            print(f"{burger.name} x {quantity} - ${burger.get_price() * quantity:.2f}")

        print("*" * 50)
        print(f"Total before tax: ${subtotal:.2f}")
        print(f"Tax Amount: ${tax:.2f}")
        print(f"Total price after tax: ${total:.2f}\n")

    def save_bill_to_file(self, subtotal, tax, total):
        with open("bill.txt.", "w") as file:
            file.write("Your Bill:\n")
            file.write("*" * 50 + "\n")
            
            for burger, quantity in self.items:
                file.write(f"{burger.name} x {quantity} - ${burger.get_price() * quantity:.2f}\n")
            file.write("*" * 50 + "\n")
            
            file.write(f"Total before tax: ${subtotal:.2f}\n")
            file.write(f"Tax Amount: ${tax:.2f}\n")
            file.write(f"Total price after tax: ${total:.2f}\n")
            
