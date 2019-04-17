"""
Permutations & Combinations
"""

# Create two functions:
	# One that outputs the **number** of possible **permutations** of rolling two 6-sided dice and assigns it to a variable called "permutations".
	# One that outputs the **number** of possible **combinations** of rolling two 6-sided dice and assigns it to a variable called "combinations".
	# Hint: The formulas for these are below, where n is the number of possible outcomes for one trial and r is the number of outcomes you will pick at a time. The contextual difference is that order matters for permutations, meaning the same two numbers in a different order count as two unique permutations. For combinations, the order doesn't matter.

# permutation formula = n! / (n-r)!
# combination formula = n! / (n−r)!r!


import math

def perms(n,r):
  result = math.factorial(n) / math.factorial(n-r)

  result = int(result)

  return result

def combs(n,r):
  result = math.factorial(n) / (math.factorial(n-r))*math.factorial(r)

  result = int(result)

  return result

permutations = perms(6,2)
combinations = combs(6,2)

print(permutations)
print(combinations)


