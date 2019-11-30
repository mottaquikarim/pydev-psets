"""
Vehicles I 
"""

# Create a "Vehicle" class with instance attributes for "name" and "owner". 
# Add a method called "start_engine()" that prints "Vroom!". 
# Instantiate a Vehicle called "submarine" and then access all its attributes and methods for practice.

class Vehicle():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def start_engine(self):
        print('Vrrrrrooomm!')


submarine = Vehicle('Yellow Submarine', 'Sgt. Pepper')

print(submarine.category) # transportation
print(submarine.name) # Yellow Submarine
print(submarine.owner) # Sgt. Pepper
submarine.start_engine() # Vrrrrrooomm!

