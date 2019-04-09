"""
Build a Triangle - SOLUTION
"""

# Use a while loop to print a 5-level triangle of stars that looks like this:

i = 1
while i <= 5:
	print('*'*i)
	i += 1

"""
*
**
***
****
*****
"""


# PREVIEW!

# Here's what it would look like if we defined a function called triangle and told it to make that 5-level triangle. 

# def triangle(levels):
# 	i = 1
# 	while i <= levels:
# 		print('*'*i)
# 		i += 1

# triangle(5)