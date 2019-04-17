"""
Speeding Tickets - FOR FUNCTIONS UNIT
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

#########################################

passing_cars = { # license plate nums & speed
  '4GRONPH': 68,
  'Q5517FA': 70,
  'S0PNWEJ': 95,
  'OJGL6WD': 82,
  'RM23RXC': 64,
  'KH5TH8D': 100,
  'IHEHJ4P': 67,
  'SVK90LT': 73,
  'LJSV4N1': 88,
  'KDRLGXM': 91
}

def speed_checker(plate,speed):
  """return # of points to add; could be 0 for non-speeders"""
  s = speed
  p = plate

  if s <= 70:
    return plate, 0
  elif s > 70:
    over = s - 70
    new_points = int(over//5)
    return plate, new_points

def speeders(plate, new_points):
  """as needed:
      return whether driver is good
      add points to license
      suspend license
      pursue violators
      """
  p = plate
  np = new_points

  driver_points = { # license plate nums & points
  '4GRONPH': 8,
  'Q5517FA': 7,
  'S0PNWEJ': 2,
  'OJGL6WD': 12,
  'RM23RXC': 6,
  'KH5TH8D': 10,
  'IHEHJ4P': 10,
  'SVK90LT': 5,
  'LJSV4N1': 3,
  'KDRLGXM': 9
  }

  if driver_points[p] >= 12:
    return f'{plate}: Violating license suspension! CAR CHASE!!!'
  elif driver_points[p] < 12 and np == 0:
    return f'{plate}: Good'
  elif driver_points[p] < 12 and np > 0:
    np = driver_points[p] + np
    driver_points.update({p: np})
    # Now that we added the new points, check if the driver still has < 12 points
    if driver_points[p] < 12:
      return f'{plate}: Points added. Catch the speeder!'
    elif driver_points[p] >= 12:
      driver_points.update({p: 'License Suspended'})
      return f'{plate}: Points added and license suspended. CAR CHASE!!!'
  else:
    return 'Tech Malfunction'



# Call the functions using values from each passing car

for k, v in passing_cars.items():
  plate = k
  speed = v
  speed_check_return = speed_checker(plate, speed)
  plate, new_points = speed_check_return
  result = speeders(plate, new_points)
  print(result,'\n')
