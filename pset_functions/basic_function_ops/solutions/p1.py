"""
Function Basics I - No Input
"""

# Write a and call a function called "rand_list" that generates a list of 5 random numbers between 1 and 500. Print out that list.

from random import randint

def rand_list():

	rand_nums = []

	i = 1

	while i <=5:
		n = randint(1,500)
		rand_nums.append(n)
		i += 1

	return rand_nums


x = rand_list()
print(x)