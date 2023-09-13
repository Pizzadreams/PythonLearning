# Lists in Python are ordered, mutable, and store heterogenous collection of objects

# Create a Python List Using the list() Function
my_list = list(range(1, 11))  # Creates a list of numbers from 1 to 10

# Display the initial list
print("Initial List:", my_list)

# sort() method - Sort the list in ascending order
my_list.sort()
print("Sorted List (Ascending):", my_list)

# type() function - Check the data type of the list
print("Data Type of List:", type(my_list))

# append() method - Add an element to the end of the list
my_list.append(11)
print("List After Append:", my_list)

# extend() method - Extend the list by appending another list to it
my_list.extend([12, 13, 14, 15, 16])
print("List After Extend:", my_list)

# index() method - Find the index of a specific element
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)

# max() function - Find the maximum value in the list
maximum_value = max(my_list)
print("Maximum Value:", maximum_value)

# min() function - Find the minimum value in the list
minimum_value = min(my_list)
print("Minimum Value:", minimum_value)

# len() function - Get the length (number of elements) of the list
list_length = len(my_list)
print("List Length:", list_length)

# clear() method - Clear all elements from the list
my_list.clear()
print("List After Clear:", my_list)

# insert() method - Insert an element at a specific index
my_list.insert(0, 'Hola, Mundo!')
print("List After Insert:", my_list)

# count() method - Count the number of occurrences of an element
list_100 = [100, 100, 100, 1000000, 100]
count_of_100 = list_100.count(100)
print("Count of 100:", count_of_100)

# pop() method - Remove and return an element at a specific index
popped_element = my_list.pop(0)
print("Popped Element:", popped_element)

# remove() method - Remove the first occurrence of a specific element
list_a = ['a', 'b', 'c', 'd']
print(f"list_a: {list_a}")
list_a.remove('d')
print("list_a after remove():", list_a)

# reverse() method - Reverse the order of elements in the list
list_b = ['red', 'orange', 'yellow', 'green', 'blue']
print(f"list_b: {list_b}")
list_b.reverse()
print("Reversed list_b:", list_b)

# copy() method - Returns a copy of the specified list; Creates a new list
list_c = ['circle', 'square', 'triangle', 'rectangle']
print(f"list_c: {list_c}")
list_c_copy = list_c.copy()
print("list_c copy:", list_c_copy)

# filter() function - Use filter() to filter elements based on a condition
def filter_function(num):
    if num % 2 == 0:
        return num
    else:
        return

list_d = [14, 2, 10, 1, 4, 3, 7, 124, 612, 19287]
print(f"list_d: {list_d}")
filtered_output = filter(filter_function, list_d)
print(f"list_d filtered: {list(filtered_output)}")
