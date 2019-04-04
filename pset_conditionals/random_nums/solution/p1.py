"""
Generate Traffic Light
"""

# import python randomint package
import random

# generates a random number from 1 to 3
randn = random.randint(1, 3)

if randn == 1:
    print('red')
if randn == 2:
    print('green')
if randn == 3:
    print('yellow')
# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'yellow'
