"""
Dogs I - Breeds
""" 

# A) Create a class called "Dog". It should include: 
### A class attribute "domesticated" w. value True
### An instance method called "bark()" that prints "Woof!"

# B) Create child class for 3 dog breeds - Collie, Siberian Husky, and Pekingese. Each should have:
### 2 class attributes for "breed" and "temperament". The latter should be a list.
### 3 instance attributes for "name", "age", and "gender".

# C) Add an instance method to Collie called "herd_the_kids()" that prints "Here are your children!"

# D) Add an instance method called "bark()" to Pekingese. This should override the parent method "bark()" such that when you call bark() on an instance of Pekingese, it prints "Yap!" instead.

# E) Instantiate one of each breed. Access the attributes, methods, and parent methods of each one. BONUS: Aside from herd_the_kids(), you should be able to do this in a loop.

### A)
class Dog():
    def __init__(self, name):
        self.name = name

    domesticated = True

    def bark(self):
        print('Woof!')

### B)
class Collie(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'collie'
    temperament = ['devoted', 'graceful', 'athletic', 'intelligent']

    ### C)
    def herd_the_kids(self):
        print('Here are your children!')

class SiberianHusky(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'husky'
    temperament = ['outgoing', 'independent', 'loyal', 'mischevious']

class Pekingese(Dog):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    breed = 'pekingese'
    temperament = ['affectionate', 'calm', 'loyal']

    ### D)
    def bark(self):
        print('Yap!')


### E)
lassie = Collie('Lassie', 3, 'female')
aiden = SiberianHusky('Aiden', 5, 'male')
cameron = Pekingese('Cameron', 8, 'female')

dogs = [lassie, aiden, cameron]

for i in dogs:
  print(f'''
{i.name}
{i.breed}
{i.domesticated}
{i.age}
{i.gender}
{i.temperament}''')
  i.bark()

print('\n')

lassie.herd_the_kids()
