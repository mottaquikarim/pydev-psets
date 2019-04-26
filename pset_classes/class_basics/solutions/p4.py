"""
Circle
"""

# Write a Python class named "Circle" constructed by a radius value. It should include two methods to calculate the "area" and the "perimeter" of a circle. Instantiate a Circle and call both methods. You can use 3.14 for the value of pi for simplicity.


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

circle1 = Circle(12)
print(circle1.area()) # 452.16
print(circle1.perimeter()) # 75.36