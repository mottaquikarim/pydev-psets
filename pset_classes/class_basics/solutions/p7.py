"""
Vehicles III
"""

# Let's expand the Car class to be more comprehensive. Include attributes for brand name, plates, owner, fuel, fuel_level (a numerical amount that defaults to 50, and max speed in MPH that defaults to None. 

# Next, define new method called "check_fuel_level()". If the fuel_level attribute is < 15, the method should reset fuel_level to 50 and print out how many units it refueled the car, e.g. 'Refueled 38 units.' Otherwise, it should simply print 'No need to refuel right now.'

# Create at least TWO instances of Car, one of which has a fuel level below 15. Access the new attributes and call the check_fuel_level() method for each instance.


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
        
    def check_fuel_level(self):
        if self.fuel_level < 15:
            diff = 50 - self.fuel_level
            self.fuel_level += diff
            return print(f'Refueled {diff} units.')
        else:
            return print('No need to refuel right now.')


ferrari1 = Car('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline', max_speed_mph = 217)

tesla1 = Car('Tesla', '8CAJ 300', 'Nicole Jackson', 'battery', 12, 155)



print(f'The {ferrari1.brand} with plate {ferrari1.plates} belongs to {ferrari1.owner} and can go up to {ferrari1.max_speed_mph} mph!') # The Ferrari with plate BD51 SMR belongs to Claude Dupont and can go up to 217 mph!
print(f'The {tesla1.brand} with plate {tesla1.plates} belongs to {tesla1.owner} and can go up to {tesla1.max_speed_mph} mph!') # The Tesla with plate 8CAJ 300 belongs to Nicole Jackson and can go up to 155 mph!

print('\n')

print(f'A {ferrari1.brand} runs on {ferrari1.fuel}, while a {tesla1.brand} runs on {tesla1.fuel}.') # A Ferrari runs on gasoline, while a Tesla runs on battery.

print('\n')

ferrari1.check_fuel_level() # No need to refuel right now.

print('\n')

tesla1.check_fuel_level() # Refueled 38 units!

