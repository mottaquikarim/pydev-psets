"""
Dogs II
""" 

# Create child class for 3 dog breeds - Collie, Siberian Husky, and Pekingese. Each should have:
## 2 class attributes for "breed" and "temperament". The latter should be a list.
## 3 instance attributes for "name", "age", and "gender".


class Dog():
    def __init__(self, name):
        self.name = name

    domesticated = True

    def bark(self):
        print('Woof!')

# Collie
class Collie(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'collie'
    temperament = ['devoted', 'graceful', 'athletic', 'intelligent']

# Husky
class SiberianHusky(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'husky'
    temperament = ['outgoing', 'independent', 'loyal', 'mischevious']


# Pekingese
class Pekingese(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'pekingese'
    temperament = ['affectionate', 'calm', 'loyal']
