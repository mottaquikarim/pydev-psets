"""
Build a Diamond - SOLUTION
"""

# Use a while loop to print a diamond of stars, like this:

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
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
  if stars % 2 != 0:
    spaces = int((chars - stars) / 2)
    print(' '*spaces+'*' * stars+' '*spaces)
  stars -= 1


# PREVIEW

# Here's what it would look like if we defined a function called pyramid and told it to make that diamond of stars. 

# def diamond(levels):
#   stars = 1
#   rows = levels
#   chars = (rows - 1) + rows
#   while stars <= chars:
#     if stars % 2 != 0:
#       spaces = int((chars - stars) / 2)
#       print(' '*spaces+'*' * stars+' '*spaces)
#     stars += 1

#   while stars >= 1:
#     if stars % 2 != 0:
#       spaces = int((chars - stars) / 2)
#       print(' '*spaces+'*' * stars+' '*spaces)
#     stars -= 1


# diamond(5)