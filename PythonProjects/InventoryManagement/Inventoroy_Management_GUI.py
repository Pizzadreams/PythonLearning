# Develop an inventory management system where you can keep track of available items and their quantities.
import tkinter as tk
import os

# Create the GUI window
root = tk.Tk()
root.title("VexIM - Inventory Management Program")

items_dict = {}

def validate_option_input(user_input, allowed_options):
    while True:
        if user_input.lower() in allowed_options:
            return user_input.lower()
        update_display("Invalid input. Please enter a valid option.")
        user_input = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ")

def validate_item_input():
  while True:
    item = input("Please enter a valid item name: ")
    if item.strip().isalpha():
        return item.lower()
    update_display("Invalid input. Please enter a valid item name.")

def validate_quantity_input():
    while True:
        quantity = input("Please enter the quantity to add: ")
        if quantity.strip().isdigit() and int(quantity) > 0:
            return int(quantity)
        update_display("Invalid input. Please enter a positive quantity.")

def view_items(items_dict):
    if not items_dict:
        update_display("The inventory is empty.")
    else:
        update_display("Here is your inventory:")
        for item, quantity in items_dict.items():
          update_display(f"\t{item.capitalize()}: {quantity}")

def add_item(items_dict):
    item = validate_item_input()
    quantity = validate_quantity_input()
    items_dict.setdefault(item, 0)
    items_dict[item] += int(quantity)
    update_display(f"You have added {quantity} {item.capitalize()}{'(s)'}. Total count: {items_dict[item]}")
    # update_display(f"You have added {quantity} {item.capitalize()}{'(s)'}. Total count: {items_dict[item]}")


"""Removes item(s) from the inventory with help of validate_quantity_to_remove()"""
def remove_item(items_dict):
    item = validate_item_input()
    if item in items_dict:
        quantity_in_inventory = items_dict[item] # retrieve the current quantity of the item from the dictionary
        if quantity_in_inventory == 1:
            del items_dict[item]
            update_display(f"{item.capitalize()} has been removed from the inventory.")
        else: # if quantity to remove is less than the current quantity in the inventory, the 'else' will execute
            quantity_to_remove = validate_quantity_to_remove(quantity_in_inventory)
            if quantity_to_remove == quantity_in_inventory:
                del items_dict[item] # deletes the key from the dictionary if the quantity_to_remove matches the quantity_in_inventory
                update_display(f"All {quantity_in_inventory} {item.capitalize()}{'(s)' if quantity_in_inventory > 1 else ''} have been removed from the inventory.")
            else:
                items_dict[item] -= quantity_to_remove # remove the amount specified from the amount if items in the dictionary
                update_display(f"{quantity_to_remove} {item.capitalize()}{'(s)' if quantity_to_remove > 1 else ''} have been removed from the inventory.")
    else:
        update_display(f"{item.capitalize()} does not exist in the inventory.")

def validate_quantity_to_remove(max_quantity):
    """Validate the quantity to remove from an item when using the 'remove_item()'."""
    while True:
        quantity = input(f"Please enter the quantity to remove (1 to {max_quantity}): ") 
        if quantity.isdigit() and 1 <= int(quantity) <= max_quantity:
            return int(quantity)
        update("Invalid input. Please enter a valid quantity.")

# Function to update the display label with the provided text
def update_display(text):
    display_label.config(text = text)

# Function to handle button click events
def handle_button_click():
    option = option_entry.get().strip().lower()
    if option == 'add':
        add_item()
    elif option == 'remove':
        remove_item()
    elif option == 'view':
        view_items()
    elif option == 'quit':
        root.quit()
    else:
        update_display("Invalid option. Please try again.")


# Create and pack the widgets in the GUI
display_label = tk.Label(root, text="Salutations. I am VexIM, your Inventory Management program.")
display_label.pack()

option_label = tk.Label(root, text="Enter 'add' to add an item, 'remove' to remove an item, 'view' to view the inventory, or 'quit' to exit:")
option_label.pack()

option_entry = tk.Entry(root)
option_entry.pack()

quantity_label = tk.Label(root, text="Please enter the quantity to add:")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

remove_quantity_label = tk.Label(root, text="Please enter the quantity to remove:")
remove_quantity_label.pack()

remove_quantity_entry = tk.Entry(root)
remove_quantity_entry.pack()

input_button = tk.Button(root, text="Submit", command=handle_button_click)
input_button.pack()

def main():
    root.mainloop()

if __name__ == '__main__':
    # os.system('cls' if os.name == 'nt' else 'clear')
    main()