"""
Play RPS w/Bad Input
"""

p1 = None  # can be invalid!
p2 = None  # can be invalid!

"""
This is the same as the original RPS problem, 
except that cannot expect the input to be valid. 
While we *want* `r` or `p` or `s`, there is a possibility 
that input can be anything like...

* `ROCK` (all caps)
* `R` (`r` but capitalized)
* `PAPrrRR` (incorrectly spelled, upper/lowercased)

Implement conditional statements that will sanitize the 
user input or let user know that input is invalid.
"""


p1 = input('Choose r, p , or s, Player 1: ')  # from user input
p2 = input('Choose r, p , or s, Player 2: ')  # from user input


##### with data that must be corrected by user

p1 = 'R'
p2 = 'ROCK'

p1 = p1.lower()
p2 = p2.lower()


if p1 == 'r' or 'p' or 's':
    val1 = True
else:
	print("Player 1, please enter 'r', 'p', or 's' in the correct format.")

if p2 == 'r' or 'p' or 's':
    val2 = True
else:
	print("Player 2, please enter 'r', 'p', or 's' in the correct format.")



#### with data that can be sanitized

p1 = 'R'
p2 = 'p'

p1 = p1.lower()
p2 = p2.lower()

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