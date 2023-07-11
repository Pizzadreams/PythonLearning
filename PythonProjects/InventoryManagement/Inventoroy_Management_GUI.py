# Develop an inventory management system where you can keep track of available items and their quantities.
import tkinter as tk
import os

# Create the GUI window
root = tk.Tk()
root.title("VexIM - Inventory Management Program")
root.geometry("550x400")
items_dict = {}

def hide_welcome_label():
    label.pack_forget()

def clear_entry_fields():
    option_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def hide_option_and_quantity_fields():
    option_entry.pack_forget()  # Hide the option_entry field
    quantity_entry.pack_forget()  # Hide the quantity_entry field

def view_items():
    hide_welcome_label()
    hide_option_and_quantity_fields()


    if not items_dict:
        update_display("The inventory is empty.")
    else:
        inventory_text = "Here is your inventory:\n"
        for item, quantity in items_dict.items(): # Concatenate the inventory items 
            inventory_text += f"{item.capitalize()}: {quantity}\n" 
        update_display(inventory_text)

"""Add item(s) to the inventory with the help of validation methods for item and quantity."""
def add_item():
    hide_welcome_label()
    option_entry.pack()
    quantity_entry.pack()
    
    update_display("Please enter a valid item and quantity amount to add.")
    
    # Check if the option_entry and quantity_entry widgets are in the window.
    if option_entry.winfo_ismapped() and quantity_entry.winfo_ismapped():
        update_display("Please add a valid item and quantity in the text fields.")
        
        item = validate_item_input()
        quantity = validate_quantity_input()

        try: # Ensure the quantity and items are not 'None'
            if quantity is None:
                raise ValueError("Invalid quantity. Please enter a positive quantity.")
            if item is None:
                raise ValueError("Invalid item. Please enter a valid item name.")
            
            items_dict.setdefault(item, 0)
            items_dict[item] += quantity
            update_display(f"You have added {quantity} {item.capitalize()}{'(s)'}. Total count: {items_dict[item]}")
        except ValueError as e:
            update_display(str(e))
            
        clear_entry_fields()
    else:
        quantity = None  # Default value when fields are not visible

"""Removes item(s) from the inventory with help of validate_quantity_to_remove()"""
def remove_item():
    hide_welcome_label()
    option_entry.pack()
    quantity_entry.pack()

    # Check if the option_entry and quantity_entry widgets are in the window.
    if option_entry.winfo_ismapped() and quantity_entry.winfo_ismapped():
        update_display("Please enter a valid item and quantity amount to remove.")

        try:
            item = validate_item_input()
            quantity = validate_quantity_input()

            if item in items_dict:
                quantity_in_inventory = items_dict[item]
                if quantity_in_inventory == 1:
                    del items_dict[item]
                    update_display(f"{item.capitalize()} has been removed from the inventory.")
                elif quantity is not None and quantity > quantity_in_inventory:
                    update_display(f"The quantity to remove exceeds the available \nquantity of {item.capitalize()} in the inventory.")
                elif quantity is not None: # check if quantity is not 'None' before performing the comparison or subtracting it from the inventory
                    items_dict[item] -= quantity
                    update_display(f"{quantity} {item.capitalize()}{'(s)' if quantity > 1 else ''} have been removed from the inventory.")
                else:
                    update_display("Invalid input. Please enter a positive number.")
            else:
                update_display(f"{item.capitalize()} does not exist in the inventory.")
        except AttributeError:
            update_display("Invalid item. Please enter a valid item name.")
        except ValueError as e:
            update_display(str(e))

    clear_entry_fields()

# def remove_item():
#     hide_welcome_label()
#     option_entry.pack()
#     quantity_entry.pack()

#     item = validate_item_input()
#     if item in items_dict:
#         quantity_in_inventory = items_dict[item] # retrieve the current quantity of the item from the dictionary
#         if quantity_in_inventory == 1:
#             del items_dict[item]
#             update_display(f"{item.capitalize()} has been removed from the inventory.")
#         else: # if quantity to remove is less than the current quantity in the inventory, the 'else' will execute
#             quantity_to_remove = validate_quantity_to_remove(quantity_in_inventory)
#             if quantity_to_remove == quantity_in_inventory:
#                 del items_dict[item] # deletes the key from the dictionary if the quantity_to_remove matches the quantity_in_inventory
#                 update_display(f"All {quantity_in_inventory} {item.capitalize()}{'(s)' if quantity_in_inventory > 1 else ''} have been removed from the inventory.")
#             else:
#                 items_dict[item] -= quantity_to_remove # remove the amount specified from the amount if items in the dictionary
#                 update_display(f"{quantity_to_remove} {item.capitalize()}{'(s)' if quantity_to_remove > 1 else ''} have been removed from the inventory.")
#     else:
#         update_display(f"{item.capitalize()} does not exist in the inventory.")
    
#     clear_entry_fields()

def validate_option_input(user_input, allowed_options):
    while True:
        if user_input.lower() in allowed_options:
            return user_input.lower()
        update_display("Invalid input. Please enter a valid option.")

def validate_item_input():
    item = option_entry.get().strip()
    if item.strip().isalpha():
        return item.lower()
    update_display("Invalid input. Please enter a valid item name.")

def validate_quantity_input():
    quantity = quantity_entry.get().strip()
    if quantity.isdigit() and int(quantity) > 0:
        return int(quantity)
    else:
        update_display("Invalid input. Please enter a positive quantity.")
        return None

def validate_quantity_to_remove(max_quantity):
    # Entry field for quantity
    quantity_entry.pack()
    """Validate the quantity to remove from an item when using the 'remove_item()'."""
    quantity = quantity_entry.get()  # Get the value from the quantity_entry field
    quantity_entry.delete(0, tk.END)  # Clear the quantity_entry field
    if quantity.isdigit() and 1 <= int(quantity) <= max_quantity:
        return int(quantity)
    update_display("Invalid input. Please enter a valid quantity.")

# Function to update the display label with the provided text
def update_display(text):
    display_label.config(text = text)

def quit_program():
    hide_welcome_label()
    hide_option_and_quantity_fields()
    update_display("Thank you for using VexIM.")
    root.after(2000, root.destroy)
    
    # Hide all buttons
    add_button.pack_forget()
    remove_button.pack_forget()
    view_button.pack_forget()
    quit_button.pack_forget()
    

quantity_entry = tk.Entry(root)
option_entry = tk.Entry(root)

display_label = tk.Label(root, text="I am VexIM, your Inventory Management program.", font=("Arial", 14))
display_label.pack()

# Label for instructions with options
label = tk.Label(root, text="Please select an option:", font=("Arial", 12))
label.pack()

# Button for adding an item
add_button = tk.Button(root, text="Add", command=add_item, font=("Arial", 12))
add_button.pack()

# Button for removing an item
remove_button = tk.Button(root, text="Remove", command=remove_item, font=("Arial", 12))
remove_button.pack()

# Button for viewing items
view_button = tk.Button(root, text="View", command=view_items, font=("Arial", 12))
view_button.pack()

# Button for quitting the program
quit_button = tk.Button(root, text="Quit", command=quit_program, font=("Arial", 12))
quit_button.pack()

root.mainloop()
