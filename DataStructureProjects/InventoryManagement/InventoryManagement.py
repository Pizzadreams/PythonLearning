# Develop an inventory management system where you can keep track of available items and their quantities.

print("Salutations. I am VexIM, your Inventory Management program.") # Validate Encrpt eXamine Inventory Management (WIP)
itemsDict = {}

def add_item():
  item = input("Please tell me what you would like to add to your inventory: ")
  quantity = int(input("Enter the quantity of the item: "))

add_item()

# print("Here is your inventory: " + str(itemsDict))
print(f"Here is your inventory: {itemsDict}")

  # # Add item to dictionary
  # itemsDict.setdefault(item, quantity)
  # for items in item:
  #   if items in item:
  #     itemsDict.setdefault(items, 0)
  #     itemsDict[items] += 1
  # for k, v in sorted(itemsDict.items()):
  #   print(k, 'was found', v, 'times(s).')
