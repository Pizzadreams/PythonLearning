# Develop an inventory management system where you can keep track of available items and their quantities.
import os 
import time

print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrypt eXamine Inventory Management (WIP)

items_dict = {}
def validate_option_input(user_input, allowed_options):
    while True:
        if user_input.lower() in allowed_options:
            return user_input.lower()
        print("Invalid input. Please enter a valid option.")
        wait_for_enter()
       # user_input = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ")

def validate_item_input():
  while True:
    item = input("Please enter a valid item name: ")
    if item.strip().isalpha():
        return item.capitalize()
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
          print(f"\t{item}: {quantity}")

def add_item(items_dict):
    item = validate_item_input()
    quantity = validate_quantity_input()
    items_dict.setdefault(item, 0)
    items_dict[item] += int(quantity)
    #print(f"You have added {quantity} {item.capitalize()}{'s' if quantity > 1 else ''}. Total count: {items_dict[item]}")
    print(f"You have added {quantity} {item}{'s' if int(quantity) > 1 else ''}. Total count: {items_dict[item]}")

def wait_for_enter():
    input("Press Enter to continue...")
    
wait_for_enter()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("Salutations. I am VexIM, your Inventory Management program.")
    items_dict = {}
    
    while True:
        option = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ")
        option = validate_option_input(option, ['add', 'view', 'quit'])

        if option == 'quit':
            print("Thank you for using VexIM.")
            break
        elif option == 'add':
            add_item(items_dict)
        
        elif option == 'view':
            view_items(items_dict)
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    main()