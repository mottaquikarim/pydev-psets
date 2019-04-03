"""
Generate Traffic Light
"""

# import python randomint package
import random

# generates a random number from 1 to 3
randn = random.randint(1, 3)
print('here', randn)
if randn == 1:
    print('red')
# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'blue'
