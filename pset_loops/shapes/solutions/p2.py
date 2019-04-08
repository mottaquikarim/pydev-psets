"""
Build a Pyramid - SOLUTION
"""

# Use a while loop to print a 5-level pyramid of stars that looks like this:

"""
    *
   ***
  *****
 *******
*********
"""

stars = 1
rows = 5
chars = (rows - 1) + rows

while stars <= chars:
  if stars % 2 != 0:
    spaces = int((chars - stars) / 2)
    print(' '*spaces+'*' * stars+' '*spaces)
  stars += 1

while stars >= 1:


# PREVIEW!

# Here's what it would look like if we defined a function called pyramid and told it to make that 5-level pyramid. 

# def pyramid(levels):
# 	stars = 1
# 	rows = levels
# 	chars = (rows - 1) + rows

# 	while stars <= chars:
# 	  if stars % 2 != 0:
# 	    spaces = int((chars - stars) / 2)
# 	    print(' '*spaces+'*' * stars+' '*spaces)
# 	  stars += 1

# pyramid(5)