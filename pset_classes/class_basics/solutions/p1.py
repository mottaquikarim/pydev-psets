"""
Person class
"""

# Create a Person class with the following properties
# 1. name
# 2. age
# 3. social security number


class Person:
    def __init__(self, name, age, social_number):
        self.name = name
        self.age = age
        self.social = social_number


p1 = Person("John", 36, "111-11-1111")

print(p1.name)
print(p1.age)
print(p1.social)
