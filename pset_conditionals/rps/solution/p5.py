"""
Play RPS against Computer
"""

p1 = None  # from user input - we still want validation from above!
p2 = None  # randomly generated against computer

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"


import random


# obtain and validate user value
p1 = input('Choose r, p , or s, Player 1: ')
p1 = p1.lower()
if p1 == 'r' or 'p' or 's':
    val1 = True
else:
	print("Player 1, please enter 'r', 'p', or 's' in the correct format.")


# generate computer value
import random

p2 = random.randint(1, 3)
if p2 == 1:
    p2 = 'r'
elif p2 == 2:
    p2 = 'p'
else:
    p2 = 's'


# game play logic
if p1 == p2:
    print(0)
elif p1 == 'r' and p2 == 's':
    print(1)
elif p1 == 'r' and p2 == 'p':
    print(2)
elif p1 == 'p' and p2 == 's':
    print(2)
elif p1 == 'p' and p2 == 'r':
    print(1)
elif p1 == 's' and p2 == 'r':
    print(2)
elif p1 == 's' and p2 == 'p':
    print(1)