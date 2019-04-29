"""
Vehicles I 
"""

# Create a "Vehicle" class with a class attribute for category ('transportion') and a method called "start_engine()" that prints "Vroom!". Add "name" and "owner" as instance attributes and instantiate a Vehicle called "submarine". Access all its attributes and methods for practice.

# Note: See Vehicles II in p6 for an explanation of why we chose "submarine" as a vehicle instance!

class Vehicle():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    category = 'transportation'

    def start_engine(self):
        print('Vrrrrrooomm!')


submarine = Vehicle('Yellow Submarine', 'Sgt. Pepper')

print(submarine.category) # transportation
print(submarine.name) # Yellow Submarine
print(submarine.owner) # Sgt. Pepper
submarine.start_engine() # Vrrrrrooomm!

