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


total1 = sum_multiples(3,17,12)
print(total1)

total2 = sum_multiples(4,9,21)
print(total2)

total3 = sum_multiples(9,21,6)
print(total3)
