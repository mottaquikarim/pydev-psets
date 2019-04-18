"""
Speeding Tickets
"""

# Imagine you're a cop waiting on the side of the road to pick up speeders. Write a function called "speeders" to check the speed of drivers and record their license plate numbers.
## If speed is less than or equal 70 (mph), it should print "Good". 
## If the speed is greater than 70, find the license plate number of that driver in your "driver_points" dict (see below) and add a point to their license for every 5 full mph above the speed limit.
## If at any point that driver has 12 or more points on his/her license, print "License Suspended".
## Call the function on each driver in the "passing_cars" dict below to see difference use cases work.

# p.s. Feel free to move these around in your code as needed.
passing_cars = { # license plate nums & speed
  '4GRONPH': 68,
  'OJGL6WD': 82,
  'Q5517FA': 70,
  'S0PNWEJ': 95,
  'RM23RXC': 64,
  'KH5TH8D': 100,
  'IHEHJ4P': 67,
  'SVK90LT': 73,
  'LJSV4N1': 88,
  'KDRLGXM': 91
}

driver_points = { # license plate nums & points
  '4GRONPH': 8,
  'OJGL6WD': 12,
  'Q5517FA': 1,
  'S0PNWEJ': 2,
  'RM23RXC': 6,
  'KH5TH8D': 7,
  'IHEHJ4P': 10,
  'SVK90LT': 5,
  'LJSV4N1': 3,
  'KDRLGXM': 9
  }


