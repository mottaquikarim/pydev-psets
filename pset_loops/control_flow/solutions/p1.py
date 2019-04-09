"""
Control Flow I - SOLUTION
"""

# Print the numbers in the range (5:12) until you find a factor of 4. If the range the user enters contains no factors of 4, print "There are no factors of 4 in this interval."

for i in range(5:12):
	if i % 4 != 0:
		print(i)
	elif i % 4 == 0:
		break
else:
	("There are no factors of 4 in this interval.")
