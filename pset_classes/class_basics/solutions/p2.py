"""
Cat class
"""

# Implement a class called "Cat" with the following properties:
# name
# breed
# age

# also, implement a method called "speak" that should print out "purr"


class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        print('purr')


c = Cat("test", "test", 5)
c.speak()
