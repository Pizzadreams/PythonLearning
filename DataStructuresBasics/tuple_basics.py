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
    
    transposed_animals = zip(*animals)

    print("'Type' of animals:", type(animals).__name__)

    # Display animals side by side
    for animal in transposed_animals: # iterate over each tuple 
        animal_info = " | ".join(str(info).ljust(8) for info in animal) # convert each item in the 'animal' tuple to a string, and separate them by the '|'
        print(animal_info)
    print()
    # for animal in animals:
    #     species, sex, age in animal
    #     print("Species:", species)
    #     print("Sex:", sex)
    #     print("Age:", age)
    #     print()

def display_cars():
    cars = (
        ("Toyota", "Camry", 2020),
        ("Honda", "Accord", 2014),
        ("Ford", "Mustang", 2011),
        ("Chevrolet", "Cruze", 2017),
    )

    print("'Type' of cars:", type(cars).__name__)

    makes, models, years = zip(*cars)

    print("Make:", ", ".join(makes))
    print("Model:", ", ".join(models))
    print("Year:", ", ".join(map(str, years)))
    print()

    # for make, model, year in cars:
    #     print("Make:", make)
    #     print("Model:", model)
    #     print("Year:", year)
    #     print()


display_animals()
display_cars()
