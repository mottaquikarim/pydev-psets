"""
Sign of Product
"""

# Given three numbers, a, b, c, without multiplying, determine the sign of their product. If it's positive, print 1. If it's negative print -1.

# EXAMPLE: a = 5, b = 6, c = -4, print -1

a = -10
b = 2
c = -6


if a < 0:
	if b < 0:
		if c < 0:
			print(-1)
		elif c > 0:
			print(1)
	elif b > 0:
		if c < 0:
			print(1)
		elif c > 0:
			print(-1)
elif a > 0:
	if b < 0:
		if c < 0:
			print(1)
		elif c > 0:
			print(-1)
	elif b > 0:
		if c < 0:
			print(-1)
		elif c > 0:
			print(1)