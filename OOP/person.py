"""
1.) Creates a class to serve as the blueprint for creating objects.
2.) Use "__init__" as it is the constructor that is executed when an object is created from the class.
3.) Create method "introduce(self)" to allow objects of the class to introduce themselves by printing their name and age.
4.) Call the introduce() on the object you create.
"""


class Person:
    # __init__() ensures that the object's attributes are properly initialized when the object is created
    def __init__(self, name, age): 
        # assign the value of the parameters to their attributes of the object
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hey. My name is {self.name} and I am {self.age} years old.")


# person1 = Person("Benny", 482)
# person1.introduce()
