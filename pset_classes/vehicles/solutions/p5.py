"""
Vehicles V
"""

# Let's expand the Car class to be more comprehensive. Include attributes for...
## brand name
## plates
## owner
## fuel (e.g. gasoline, battery, etc.)
## fuel_level (a numerical amount that defaults to 50, and max speed in MPH that defaults to None.

class Vehicle():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    category = 'transportation'

    def start_engine(self):
        print('Vrrrrrooomm!')

class Car(Vehicle):
    def __init__(self, brand, plates, owner, fuel, fuel_level = 50, max_speed_mph = None):
        self.brand = brand
        self.plates = plates
        self.owner = owner
        self.fuel = fuel
        self.fuel_level = fuel_level 
        self.max_speed_mph = max_speed_mph

    motion = 'drive'
    terrain = 'land'

    def honk_horn(self):
        print('HONK!')

