"""
Multiples
"""

# Write a function called "sum_multiples" that take two numbers and returns the sum of their multiples between 0 and some limit. These three items should be generalized as parameters.


def sum_multiples(num1,num2,limit):
	"""take two numbers and find the sum of their multiples from 1 to some upper limit. this DOES NOT double-count numbers which are multiples of BOTH num1 and num2."""
	sum = 0

	if num1 > limit and num2 > limit:
		return sum

	for i in range(1,(limit+1)):
		if i % num1 == 0 or i % num2 == 0:
			sum += i

	return sum

num1 = int(input('Enter the first factor: '))
num2 = int(input('Enter the second factor: '))
limit = int(input('Enter a number for the upper limit: '))

total = sum_multiples(num1,num2,limit)

print(f'The sum of all the multiples of {num1} and {num2} up to {limit} is {total}.')