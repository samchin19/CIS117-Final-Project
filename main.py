# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

from Order import Order
from Customer import Customer
from Staff import Staff
from Student import Student
from Burgers import Burger
from BurgerClasses import BURGER_CLASSES
import tkinter

def display_menu():
    '''
    Displays the menu options for the Food Court
    '''
    print("*" * 10)
    print("Welcome to the College Food Court!")
    print("Please choose from the following:")
   for idx, burger_cls in enumerate(BURGER_CLASSES, start=1):
        burger = burger_cls()
        print(f"{idx}. {burger.name} - ${burger.price:.2f}")
    print("6. Exit")
    print("*" * 10)

def get_customer_type():
    while True:
        isStudentString = input("Are you a student? (y/n): ").strip().lower()
        if isStudentString == 'y':
            return Student()
        elif isStudentString == 'n':
            return Staff()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main(): 

    #Creating an order object 
    customerOrder = Order()

    while True: 
        display_menu()
        try: 
            burger = int(input("Please enter what burger you would like: "))
            if burger == 6:
                break
            if burger >= 1 and burger <= 5:
                while True:
                    try:
                        quantity = int(input("Please enter quantity: "))
                        if quantity > 0:
                            burger_class = BURGER_CLASSES[burger - 1]
                            burger = burger_class()
                            customerOrder.add_item(burger, quantity)
                            break
                        else:
                            print("Invalid quantity. Please enter a non-negative quantity.")
                    except ValueError:
                        print("Error, please enter a numeric input.")
            else:
                print("Invalid choice. Please select between 1-6.")
        except ValueError:
            print("Error, please enter a numeric input")

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
