"""
Weather II - Precipitation
"""

# Repeat the same process as p1, using this new set of variables.


sunny = True
raining = True
snowing = False

is_it_sunny = sunny
print(is_it_sunny) # True

is_there_precipitation = raining or snowing
print(is_there_precipitation) # True

is_it_sleeting = raining and snowing
print(is_it_sleeting) # False

is_there_rainbow = raining and sunny
print(is_there_rainbow) # True