# Develop an inventory management system where you can keep track of available items and their quantities.
import os 
import time
from requests.structures import CaseInsensitiveDict

print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrypt eXamine Inventory Management (WIP)

#items_dict = CaseInsensitiveDict()
items_dict = {}

def validate_option_input(user_input, allowed_options):
    while True:
        if user_input.lower() in allowed_options:
            return user_input.lower()
        print("Invalid input. Please enter a valid option.")
        wait_for_enter()
        user_input = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ")

def validate_item_input():
  while True:
    item = input("Please enter a valid item name: ")
    if item.strip().isalpha():
        return item.lower()
    print("Invalid input. Please enter a valid item name.")

def validate_quantity_input():
    while True:
        quantity = input("Please enter the quantity to add: ")
        if quantity.strip().isdigit() and int(quantity) > 0:
            return int(quantity)
        print("Invalid input. Please enter a positive quantity.")

def view_items(items_dict):
    if not items_dict:
        print("The inventory is empty.")
    else:
        print("Here is your inventory:")
        for item, quantity in items_dict.items():
          print(f"\t{item.capitalize()}: {quantity}")
    
    wait_for_enter()  

def add_item(items_dict):
    item = validate_item_input()
    quantity = validate_quantity_input()
    items_dict.setdefault(item, 0)
    items_dict[item] += int(quantity)
    print(f"You have added {quantity} {item.capitalize()}{'(s)'}. Total count: {items_dict[item]}")
    
    wait_for_enter()
    #print(f"You have added {quantity} {item.capitalize()}{'s' if quantity > 1 else ''}. Total count: {items_dict[item]}")

def remove_item(items_dict):
    item = validate_item_input()
    if item in items_dict:
        quantity_in_inventory = items_dict[item] # retrieve the current quantity of the item from the dictionary
        if quantity_in_inventory == 1:
            del items_dict[item]
            print(f"{item.capitalize()} has been removed from the inventory.")
        else:
            quantity_to_remove = validate_quantity_to_remove(quantity_in_inventory)
            if quantity_to_remove == quantity_in_inventory:
                del items_dict[item] # deletes the key from the dictionary if the quantity_to_remove matches the quantity_in_inventory
                print(f"All {quantity_in_inventory} {item.capitalize()}{'(s)' if quantity_in_inventory > 1 else ''} have been removed from the inventory.")
            else:
                items_dict[item] -= quantity_to_remove
                print(f"{quantity_to_remove} {item.capitalize()}{'(s)' if quantity_to_remove > 1 else ''} have been removed from the inventory.")
    else:
        print(f"{item.capitalize()} does not exist in the inventory.")
    wait_for_enter()

def validate_quantity_to_remove(max_quantity):
    '''Validate the quantity to remove from an item when using the 'remove_item()'.'''
    while True:
        quantity = input(f"Please enter the quantity to remove (1 to {max_quantity}): ") 
        if quantity.isdigit() and 1 <= int(quantity) <= max_quantity:
            return int(quantity)
        print("Invalid input. Please enter a valid quantity.")

def wait_for_enter():
    input("Press Enter to continue...")
    
wait_for_enter()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Salutations. I am VexIM, your Inventory Management program.")
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        option = input("Enter 'add' to add an item, 'remove' to remove an item, 'view' to view the inventory, or 'quit' to exit: ")
        option = validate_option_input(option, ['add', 'remove', 'view', 'quit'])

        if option == 'quit':
            print("Thank you for using VexIM.")
            break
        elif option == 'add':
            add_item(items_dict)
        elif option == 'remove':
            remove_item(items_dict)
        elif option == 'view':
            view_items(items_dict)
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()