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

def validate_item_input():
  while True:
    item = input("Please enter a valid item name: ")
    if item.strip().isalpha():
        return item
    print("Invalid input. Please enter a valid item name.")

def validate_quantity_input(quantity):
  while True:
    if not str(quantity).strip() or not str(quantity).isdigit() or int(quantity) <= 0:
      print("Invalid input. Please enter a positive integer quantity.")
      return None
    return True

def validate_option_input(input, allowed_options):
  while True:
    if input.lower() not in allowed_options:
        print("Invalid input. Please enter a valid option.")
        wait_for_enter()
        return None
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
    if option.lower() == 'quit':
        print("Thank you for using VexIM.")
        break
    elif option.lower() == 'add':
      item = validate_item_input()
      # item = validate_item_input("What would you like to add to your inventory: ").lower()
      #if not validate_item_input(item):
      #    continue
      quantity = input("Please enter the quantity to add: ")
      if not validate_quantity_input(quantity):
          continue
      # item = str(input("What would you like to add to your inventory: ").lower())
      # item = validate_item_input(item)
  
      # quantity = int(input("Please enter the quantity to add: "))
      # quantity = validate_quantity_input(quantity)
      
      itemsDict.setdefault(item, 0)
      itemsDict[item] += int(quantity)
      print(f"You have added {quantity} {item}{'s' if int(quantity) > 1 else ''}. Total count: {itemsDict[item]}")
      wait_for_enter()

    elif option == 'view':
        view_items(itemsDict)
        input("Press Enter to continue...")
    else:
        print("Invalid option. Please try again.")
