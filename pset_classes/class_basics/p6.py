"""
Vehicles II
"""

# Define 3 unique child classes for Vehicle - Car, Plane, and Boat. Each of these should have its own class attributes for "motion" and "terrain". (For Car, these would be something like "drive" and "land".)

## For Car, define a method called "honk_horn()" that prints "HONK!"
## For Plane, define a method called "take_off()" that prints "Fasten your seatbelts!"
## For Boat, define a method called "drop_achor()" that prints "Anchors away!"

# Create an instance of each child class. Access all their attributes and methods, including those inherited from their parent class Vehicle.

# TAKEAWAY! - Vehicle is the baseline class for other more specific types of vehicles. Typically, you wouldn't instantiate a Vehicle because the child classes are more useful for storing information about vehicles. The Vehicle class serves to create a relationship between its children. However, "submarine" might be created as a Vehicle because it's so rare that you might not need a full Submarine class!