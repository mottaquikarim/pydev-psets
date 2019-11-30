"""
Dog Class
"""

# Create a class called "Dog". It should include: 
## A class attribute "domesticated" w. value True
## An instance method called "bark()" that prints "Woof!"


class Dog():
    def __init__(self, name):
        self.name = name

    domesticated = True

    def bark(self):
        print('Woof!')

