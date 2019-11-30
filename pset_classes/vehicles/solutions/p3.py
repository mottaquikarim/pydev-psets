"""
Vehicles III
"""

# For Car, define a method called "honk_horn()" that prints "HONK!"
# For Plane, define a method called "take_off()" that prints "Fasten your seatbelts!"
# For Boat, define a method called "drop_achor()" that prints "Anchors away!"


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

    def honk_horn(self):
        print('HONK!')


class Plane(Vehicle):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    motion = 'fly'
    terrain = 'air'

    def take_off(self):
        print('Fasten your seatbelts!')


class Boat(Vehicle):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    motion = 'sail'
    terrain = 'water'

    def drop_anchor(self):
        print('Anchors away!')
