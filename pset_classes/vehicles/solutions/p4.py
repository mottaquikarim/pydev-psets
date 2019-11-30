"""
Vehicles IV
"""

# Create an instance of each child class. Access all their attributes and methods, including those inherited from their parent class Vehicle.

# TAKEAWAY! - Vehicle is the baseline class for other more specific types of vehicles. Typically, you wouldn't instantiate a Vehicle because the child classes are more useful for storing information about vehicles. The Vehicle class serves to create a relationship between its children. However, "submarine" might be created as a Vehicle because it's so rare that you might not need a full Submarine class!

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


# CAR INSTANCE
car1 = Car('The Batmobile','Batman')

print(car1.category) # transportation
print(car1.owner, 'can', car1.motion, car1.name, 'on', car1.terrain) # The Batmmobile can drive on land
car1.start_engine() # Vrrrrrooomm!
car1.honk_horn() # HONK!

print('\n')

# PLANE INSTANCE
plane1 = Plane('The Canary', 'Amelia Earhart')

print(plane1.category) # transportation
print(plane1.owner, 'can', plane1.motion, plane1.name, 'through the', plane1.terrain) # Amelia Earhart can fly The Canary through the air
plane1.start_engine() # Vrrrrrooomm!
plane1.take_off() # Fasten your seatbelts!

print('\n')

# BOAT INSTANCE
boat1 = Boat('Jenny', 'Forrest Gump')

print(boat1.category) # transportation
print(boat1.owner, 'can', boat1.motion, boat1.name, 'on', boat1.terrain) # Forrest Gump can sail Jenny on water
boat1.start_engine() # Vrrrrrooomm!
boat1.drop_anchor() # Anchors Away!