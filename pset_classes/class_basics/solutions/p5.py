"""
Circle
"""

# Write a Python class named "Circle" constructed by a radius value and a class attribute for pi. You can use 3.14159 for the value of pi for simplicity. It should include two methods to calculate the "area" and the "perimeter" of a circle. Instantiate a Circle and call both methods.


class Circle():
    def __init__(self, r):
        self.radius = r

    pi = 3.14159

    def area(self):
        return self.radius**2*self.pi
    
    def perimeter(self):
        return 2*self.radius*self.pi

circle1 = Circle(12)
print(circle1.area()) # 380.13239
print(circle1.perimeter()) # 69.11498