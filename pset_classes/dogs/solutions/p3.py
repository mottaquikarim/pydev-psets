"""
Dogs III
""" 

# A) Add an instance method to Collie called "herd_the_kids()" that prints "Here are your children!"

# B) Add an instance method called "bark()" to Pekingese. This should override the parent method "bark()" such that when you call bark() on an instance of Pekingese, it prints "Yap!" instead.

# C) Instantiate one of each breed. Access the attributes, methods, and parent methods of each one. 
# BONUS: Aside from herd_the_kids(), you should be able to do this in a loop.


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

    ### A)
    def herd_the_kids(self):
        print('Here are your children!')

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

    ### B)
    def bark(self):
        print('Yap!')


### C)
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
