# Develop an inventory management system where you can keep track of available items and their quantities.

print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrpt eXamine Inventory Management (WIP)
itemsDict = {}

def view_items(items_dict):
    print("Here is your inventory:")
    for item, quantity in items_dict.items():
        print(f"{item}: {quantity}")

while True:
    option = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ")

    if option == 'quit':
        break
    elif option == 'add':
        item = input("Please tell me what you would like to add to your inventory: ")
        itemsDict.setdefault(item, 0)
        itemsDict[item] += 1
    elif option == 'view':
        view_items(itemsDict)
    else:
        print("Invalid option. Please try again.")

  # # Add item to dictionary
  # itemsDict.setdefault(item, quantity)
  # for items in item:
  #   if items in item:
  #     itemsDict.setdefault(items, 0)
  #     itemsDict[items] += 1
  # for k, v in sorted(itemsDict.items()):
  #   print(k, 'was found', v, 'times(s).')
