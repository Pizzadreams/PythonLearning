# Develop an inventory management system where you can keep track of available items and their quantities.
import os 


print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrypt eXamine Inventory Management (WIP)
itemsDict = {}

def view_items(items_dict):
    if not items_dict:
        print("The inventory is empty.")
    else:
      print("Here is your inventory:")
      for item, quantity in items_dict.items():
          print(f"\t{item}: {quantity}")

def validate_item_input(item):
    if not item.strip():
        print("Invalid input. Please enter a valid item name.")
        return False
    return True

def validate_quantity_input(quantity):
    if quantity <= 0:
        print("Invalid input. Please enter a positive quantity.")
        return False
    return True

def validate_option_input(input, allowed_options):
    if input.lower() not in allowed_options:
        print("Invalid input. Please enter a valid option.")
        wait_for_enter()
        return False
    return True

def wait_for_enter():
    input("Press Enter to continue...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    # option variable is used to store the user's input 
    option = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ").lower()
    allowed_options = ['add', 'view', 'quit']
    if not validate_option_input(option, allowed_options):
      continue
    if option == 'quit':
        print("Thank you for using VexIM.")
        break
    elif option == 'add':
      item = input("What would you like to add to your inventory: ").lower()
      if not validate_item_input(item):
          # wait_for_enter()
          continue

      quantity = int(input("Please enter the quantity to add: "))
      if not validate_quantity_input(quantity):
          # wait_for_enter()   
          continue

      itemsDict.setdefault(item, 0)
      itemsDict[item] += quantity
      print(f"You have added {quantity} {item}{'s' if quantity > 1 else ''}. Total count: {itemsDict[item]}")
      input("Press Enter to continue...")

    elif option == 'view':
        view_items(itemsDict)
        input("Press Enter to continue...")
    else:
        print("Invalid option. Please try again.")
