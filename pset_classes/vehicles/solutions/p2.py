"""
Vehicles II
"""

# Define 3 unique child classes for Vehicle - Car, Plane, and Boat. Each of these should have its own class attributes for "motion" and "terrain". (For Car, these would be something like "drive" and "land".)

class Vehicle():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    category = 'transportation'

    def start_engine(self):
        print('Vrrrrrooomm!')


class Car(Vehicle):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    motion = 'drive'
    terrain = 'land'


class Plane(Vehicle):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    motion = 'fly'
    terrain = 'air'


class Boat(Vehicle):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    motion = 'sail'
    terrain = 'water'

