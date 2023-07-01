def find_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    return common_elements

def find_unique_elements(set1, set2):
    unique_elements = set1.symmetric_difference(set2)
    return unique_elements

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


print(f"set1: {set1}")
print(f"set2: {set2}")

common = find_common_elements(set1, set2)
print("Common elements:", common)

unique = find_unique_elements(set1, set2)
print("Unique elements:", unique)