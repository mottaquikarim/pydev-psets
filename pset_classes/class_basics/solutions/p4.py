"""
Rectangle
"""

# Write a Python class named "Rectangle" constructed by values for length and width. It should include two methods to calculate the "area" and the "perimeter" of a rectangle. Instantiate a Rectangle and call both methods.


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

    def perimeter(self):
    	return self.length*2 + self.width*2

rect1 = Rectangle(12, 10)
print(rect1.area()) # 120 
print(rect1.perimeter()) # 44