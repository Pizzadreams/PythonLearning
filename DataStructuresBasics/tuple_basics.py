import os
os.system('cls' if os.name == 'nt' else 'clear')

# Create a tuple of animal records
animals = (
    ("Lion", "Male", 5),
    ("Elephant", "Female", 10),
    ("Giraffe", "Male", 7),
    ("Tiger", "Female", 4),
)

print("'Type' of animals:", type(animals).__name__) # returnin gthe name of the class as a string 

# Display the details of each animal
for animal in animals:
    species, sex, age = animal
    print("Species:", species)
    print("Sex:", sex)
    print("Age:", age)
    print() 
