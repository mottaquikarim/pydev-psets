"""
Play RPS w/Input
"""

p1 = input('player 1 choice: ')  # from user input
p2 = input('player 2 choice: ')  # from user input

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

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"
