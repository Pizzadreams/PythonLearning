# Develop an inventory management system where you can keep track of available items and their quantities.

print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrypt eXamine Inventory Management (WIP)
itemsDict = {}

def view_items(items_dict):
    print("Here is your inventory:")
    for item, quantity in items_dict.items():
        print(f"{item}: {quantity}")

while True:
    # option variable is used to store the user's input 
    option = input("Enter 'add' to add an item, 'view' to view the inventory, or 'quit' to exit: ").lower() #.lower() converts input to lowercase before performing comparisons to ensure they are not case sensitive
    if option == 'quit':
        print("Thank you for using VexIM.")
        break
    elif option == 'add':
        item = input("Please tell me what you would like to add to your inventory: ")
        itemsDict.setdefault(item, 0)
        itemsDict[item] += 1
    elif option == 'view':
        view_items(itemsDict)
    else:
        print("Invalid option. Please try again.")
