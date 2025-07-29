# CIS117 - Final Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons

import tkinter


def display_menu():

def get_customer_type():

def main(): 


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
