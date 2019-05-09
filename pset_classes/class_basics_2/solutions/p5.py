"""
Vehicle class
"""

# Create a Vehicle class with the following properties

# * name
# * kind
# * color
# * value


# define the Vehicle class
class Vehicle:
	def __init__(self, name, kind, color, value):
	    self.name = name
	    self.kind = kind
	    self.color = color
	    self.value = value

    def description(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth ${self.value}."
        return desc_str

# test code
car1 = Vehicle('test', 'test', 'test', 100.00)
print(car1.description())
