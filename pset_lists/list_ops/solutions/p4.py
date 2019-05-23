"""
Ordering Random Numbers
"""

# Create a list of 6 randomly generated numbers called rand_nums and sort it in descending order.

from random import randint

rand_nums = randint(6)

sorted(rand_nums, reverse = True)