"""
Multiple Inheritance
"""

# Create a hierarchy of 3 classes with parent child relationships: Vehicle > Car > Brand of Car.
# Vehicle should have a class attribute for category ('transportion') and a method called "start_engine()" that prints "Vroom!"
# Car should have motion and terrin class attributes ('drive' and 'land' respectively). It should also have a method called "honk_horn()" that prints "HONK!"
# The brand class should have attributes for brand name, plates, owner, fuel, and max speed in MPH. It should have a method called "describe()" that prints out all these details.

# Once done creating these, instantiate at least one instance object for each class. Access attributes and call methods belonging to each instance's class and its parent class. Note that the third class will be child to BOTH Vehicle AND Car.

class Vehicle():
	def __init__(self, name):
		self.name = name

	category = 'transportation'

	def start_engine(self):
		print('Vrrrrrooomm!')


class Car(Vehicle):
	def __init__(self, type): # type ==> type of vehicle
		self.type = type

	motion = 'drive'
	terrain = 'land'

	def honk_horn(self):
		print('HONK!')

cars = Car('cars')

print(cars.category) # transportation
print(isinstance(cars, Vehicle)) # True
print(cars.type, cars.motion, 'on', cars.terrain) # cars drive on land
cars.start_engine() # Vrrrrrooomm!
cars.honk_horn() # HONK!

# Here are two other examples of child classes for Vehicle:
# class Plane(Vehicle):
# 	def __init__(self, type):
# 		self.type = type

# 	motion = 'fly'
# 	terrain = 'air'


# class Boat(Vehicle):
# 	def __init__(self, type):
# 		self.type = type

# 	motion = 'sail'
# 	terrain = 'water'




class Ferrari(Car):
	def __init__(self, name, plates, owner, fuel, max_speed_mph = None, *args):
		self.name = name
		self.plates = plates
		self.owner = owner
		self.fuel = fuel
		self.max_speed_mph = max_speed_mph

	manufac = 'S.p.A.'
	manufac_hq = 'Maranello, Italy'

	def describe(self):
		print(f'{self.name, self.plates, self.owner, self.fuel, self.max_speed_mph}')

class Tesla(Car):
	def __init__(self, name, plates, owner, fuel, max_speed_mph = None, *args):
		self.name = name
		self.plates = plates
		self.owner = owner
		self.fuel = fuel
		self.max_speed_mph = max_speed_mph

	manufac = 'S.p.A.'
	manufac_hq = 'Maranello, Italy'

	def describe(self):
		print(f'{self.name, self.plates, self.owner, self.fuel, self.max_speed_mph}')	


carA = Ferrari('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline', 217)

carB = Tesla('Tesla', '8CAJ 300', 'Nicole Jackson', 'battery', 155)

print(carA.category) # transportation
print(isinstance(carA, Vehicle)) # True
print(isinstance(carA, Car)) # True
print(carA.name, carA.motion, 'on', carA.terrain) # cars drive on land
carA.start_engine() # Vrrrrrooomm!
carA.honk_horn() # HONK!


print(f'A {carA.name} runs on {carA.fuel}, while a {carB.name} runs on {carB.fuel}.') # A Ferrari runs on gasoline, while a Tesla runs on battery.
carA.describe() # ('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline', 217)
carB.describe() # ('Tesla', '8CAJ 300', 'Nicole Jackson', 'battery', 155)