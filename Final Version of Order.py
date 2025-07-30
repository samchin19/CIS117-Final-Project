# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
import tkinter as tk
from DeAnzaBurger import DeAnzaBurger
from BaconCheeseBurger import BaconCheese
from MushroomSwissBurger import MushroomSwiss
from DonCaliBurger import DonCaliBurger
from WesternBurger import WesternBurger

class Order:
    '''
    This class represents a customer order, managing items,
    calculating totals, printing the bills, and saving to a file.
    '''

    def __init__(self):
        '''
        Initializes a new Order instance.
        '''
        self.items = [] # Stores (burger_object, quantity) tuples
        self._priceDict = { # Menu items and their prices
            "Bacon Cheese": 5.75,
            "De Anza Burger": 5.25,
            "Don Cali Burger": 5.95,
            "Mushroom Swiss": 5.95,
            "Western Burger": 5.95
        }
        self._orderDict = {  # Stores items quantity
            "Bacon Cheese": 0,
            "De Anza Burger": 0,
            "Don Cali Burger": 0,
            "Mushroom Swiss": 0,
            "Western Burger": 0
        }
        self._priceBeforeTax = 0.0
        self._taxAmount = 0.0
        self._priceAfterTax = 0.0
        self.root = None # GUI

    def get_price_dict(self):
        '''
        Returns the dictionary of menu items and their prices.
        :return: A dictionary
        '''
        return self._priceDict

    def add_item(self, burger, quant):
        '''
        Adds a burger and its quantity to the order based on user input.
        :param burger:
        :param quant:
        :return:
        '''
        burger_map = {
            1: DeAnzaBurger(),
            2: BaconCheese(),
            3: MushroomSwiss(),
            4: WesternBurger(),
            5: DonCaliBurger()
        }

        try:
            choice = int(burger)
            quantity = int(quant)
            if choice in burger_map and quantity > 0:
                burger_obj = burger_map[choice]
                self.items.append((burger_obj, quantity))
                self._orderDict[burger_obj.get_name()] += quantity
            else:
                print("Invalid burger choice or quantity.")
        except ValueError:
            print("Invalid input. Please enter numeric input.")

    def calc_total(self, customer):
        '''
        Calculates the total bill.
        :param customer:
        :return:
        '''
        self._priceBeforeTax = sum(burger.get_price() * quantity for burger, quantity in self.items)
        self._taxAmount = customer.calculate_tax(self._priceBeforeTax)
        self._priceAfterTax = self._priceBeforeTax + self._taxAmount


    def print_bill(self):
        '''
        Prints the bill to the console
        :param subtotal:
        :param tax:
        :param total:
        :return:
        '''
        print("\nYour Bill:")
        print("*" * 50)

        for burger, quantity in self.items:
            print(f"{burger.name} x {quantity} - ${burger.get_price() * quantity:.2f}")

        print("*" * 50)
        print(f"Total before tax: ${self._priceBeforeTax:.2f}")
        print(f"Tax Amount: ${self._taxAmount:.2f}")
        print(f"Total price after tax: ${self._priceAfterTax:.2f}\n")

    def save_bill_to_file(self):
        '''
        Saves the bill to a text file named "Bill.txt"
        :param subtotal:
        :param tax:
        :param total:
        :return:
        '''
        try:
            with open("Bill.txt", "w") as file:
                file.write("Your Bill:\n")
                file.write("*" * 50 + "\n")

                for burger, quantity in self.items:
                    file.write(f"{burger.name} x {quantity} - ${burger.get_price() * quantity:.2f}\n")
                file.write("*" * 50 + "\n")

                file.write(f"Total before tax: ${self._priceBeforeTax:.2f}\n")
                file.write(f"Tax Amount: ${self._taxAmount:.2f}\n")
                file.write(f"Total price after tax: ${self._priceAfterTax:.2f}\n")
        except IOError as e:
            print(f"Error saving bill to a file: {e}")

    def showOrderGUI(self):
        '''
        Displays the order in a Tkinter graphical user interface.
        '''
        print("Displaying the order in a Graphics Window")

        self.root = tk.Tk()
        self.root.attributes('-topmost', True) # Make the window always appear on top of others
        self.root.geometry("360x580")
        self.root.title("Order GUI")

        gui_frame = tk.Frame(self.root)
        gui_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True) # Fills all expandable place
        gui_frame.grid_columnconfigure(0, weight=1)
        gui_frame.grid_columnconfigure(1, weight=0)
        # Adding "Order Summary" label
        order_label = tk.Label(gui_frame, text="Your Order:", font=('Helvetica', 16, 'bold'))
        order_label.grid(row=0, column=0, columnspan=2, pady=10)

        row_num = 1
        for burger, quantity in self.items:
            item_text = f"{burger.get_name()} x {quantity}"
            price_text = f"${burger.get_price() * quantity:.2f}"

            item_label = tk.Label(gui_frame, text=item_text, anchor='w')
            item_label.grid(row=row_num, column=0, sticky=tk.W, padx=15, pady=2)

            price_label = tk.Label(gui_frame, text=price_text, anchor='e')
            price_label.grid(row=row_num, column=0, columnspan=2, pady=5)

            row_num += 1

        tk.Label(gui_frame, text="-" * 50).grid(row=row_num, column=0, columnspan=2, pady=5)
        row_num += 1

        total_before_tax_label = tk.Label(gui_frame, text=f"Total before tax: ${self._priceBeforeTax:.2f}", anchor='w')
        total_before_tax_label.grid(row=row_num, column=0, columnspan=2, sticky=tk.W, padx=5)
        row_num += 1

        tax_amount_label = tk.Label(gui_frame, text=f"Tax amount: ${self._taxAmount:.2f}", anchor='w')
        tax_amount_label.grid(row=row_num, column=0, columnspan=2, sticky=tk.W, padx=5)
        row_num += 1

        total_amount_label = tk.Label(gui_frame, text=f"Total after tax: ${self._priceAfterTax:.2f}", anchor='w', font=('Helvetica', 14, 'bold'))
        total_amount_label.grid(row=row_num, column=0, columnspan=2, sticky=tk.W, padx=5, pady=10)
        row_num += 1

        close_button = tk.Button(gui_frame, text="Close", command=self.root.destroy)
        close_button.grid(row=row_num, column=0, columnspan=2, pady=10)

        self.root.mainloop()
