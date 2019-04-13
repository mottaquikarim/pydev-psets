"""
Play RPS w/Computer
"""

import random

p1 = random.randint(1, 3)  # randomly choose 'r' or 'p' or 's'
p2 = random.randint(1, 3)  # randomly choose 'r' or 'p' or 's'

if p1 == 1:
    p1val = 'r'
elif p1 == 2:
    p1val = 'p'
else:
    p1val = 's'


if p2 == 1:
    p2val = 'r'
elif p2 == 2:
    p2val = 'p'
else:
    p2val = 's'


if p1val == p2val:
    print(0)
elif p1val == 'r' and p2val == 's':
    print(1)
elif p1val == 'r' and p2val == 'p':
    print(2)
elif p1val == 'p' and p2val == 's':
    print(2)
elif p1val == 'p' and p2val == 'r':
    print(1)
elif p1val == 's' and p2val == 'r':
    print(2)
elif p1val == 's' and p2val == 'p':
    print(1)


# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"
