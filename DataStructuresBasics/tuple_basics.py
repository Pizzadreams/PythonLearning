import os
os.system('cls' if os.name == 'nt' else 'clear')

# Create a tuple of animal records
def display_animals():
    animals = (
        ("Lion", "Male", 5),
        ("Elephant", "Female", 10),
        ("Giraffe", "Male", 7),
        ("Tiger", "Female", 4),
    )
    
    print("'Type' of animals:", type(animals).__name__)
    
    for animal in animals:
        species, sex, age = animal
        print("Species:", species)
        print("Sex:", sex)
        print("Age:", age)
        print()

def display_cars():
    cars = (
        ("Toyota", "Camry", 2020),
        ("Honda", "Accord", 2014),
        ("Ford", "Mustang", 2011),
        ("Chevrolet", "Cruze", 2017),
    )

    print("'Type' of cars:", type(cars).__name__)

    for make, model, year in cars:
        print("Make:", make)
        print("Model:", model)
        print("Year:", year)
        print()


display_animals()
display_cars()
