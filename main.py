# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

from Order import Order
from Customer import Customer
from Staff import Staff
from Student import Student
from Burgers import Burger
from BaconCheeseBurger import BaconCheese
from DeAnzaBurger import DeAnzaBurger
from DonCaliBurger import DonCaliBurger
from MushroomSwissBurger import MushroomSwiss
from WesternBurger import WesternBurger
import tkinter

def display_menu():
    '''
    Displays the menu options for the Food Court
    '''
    print("*" * 10)
    print("Welcome to the College Food Court!")
    print("Please choose from the following:")
    print("1. De Anza Burger - $5.25")
    print("2. Bacon Cheese - $5.75")
    print("3. Mushroom Swiss - $5.95")
    print("4. Western Burger - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")
    print("*" * 10)

def get_customer_type():
    while True:
        isStudentString = input("Are you a student? (y/n): ").strip().lower()
        if isStudentString == 'y':
            return Student()
        elif isStudentString == 'n':
            return RegularCustomer()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main(): 
    display_menu()

    #Creating an order object 
    customerOrder = Order()
    
    burger = input("Please enter what burger you would like: ")
    quantity = int(input("Please enter quanity: "))
    customerOrder.add_item(burger=burger, quantity=quantity)

    customer = get_customer_type()
    subtotal, tax, total = customerOrder.calc_total(customer)
    customerOrder.print_bill(subtotal, tax, total)

    #Saving the bill in a file 
    customerOrder.save_bill_to_file(subtotal, tax, total)

def displayOrderGUI(self):
    print("Displaying the order in a Graphics Window")

    gui_frame = tkinter.Frame(self.root)
    gui_frame.pack()

    # Adding "Order Summary" label
    order_label = tkinter.Label(gui_frame, text="Your Order:")
    order_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Adding label for each Order Item

    # Adding "Total" label
    total_label = tkinter.Label(gui_frame, text=f"Total: ${self.price:.2f}") # TODO: Change "price" to an actual variable

    # Adding "Close" Button
    close_button = tkinter.Button(gui_frame, text="Close application", command=self.root.destroy)
    close_button.grid(row=len(self._orderDict) +2, column=0, columnspan=2, pady=10) # TODO: Change "_orderDict" to an actual variable

    self.root.mainloop()

if __name__ == '__main__':
    main()
