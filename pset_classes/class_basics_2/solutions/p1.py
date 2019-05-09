"""
Dog Class
"""

# Implement a class called "Dog" with the following properties:
# name
# breed
# age


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


d = Dog("test", "test", 5)
print(d.name)
print(d.breed)
print(d.age)
