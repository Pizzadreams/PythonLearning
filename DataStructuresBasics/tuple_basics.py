import os
os.system('cls' if os.name == 'nt' else 'clear')

# Create a tuple of animal records
def display_animals(animals):
    print("This is a basic program using the tuple data structure.\n")
    print("'Type' of animals:", type(animals).__name__ + "\n") # returning the name of the class as a string (add .__name__)

    # Display the details of each animal
    for animal in animals:
        species, sex, age = animal
        print("Species:", species)
        print("Sex:", sex)
        print("Age:", age)
        print()

# Create a tuple of animal records
animals = (
    ("Lion", "Male", 5),
    ("Elephant", "Female", 10),
    ("Giraffe", "Male", 7),
    ("Tiger", "Female", 4),
)

# Call the function with the animals tuple
display_animals(animals)