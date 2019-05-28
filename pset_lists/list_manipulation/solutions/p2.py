"""
Basic Math Ops
"""

# Given the list below, assign the correct values to the variables below.
	# my_sum = 
	# my_min = 
	# my_max = 
	# my_range = 
	# my_mean =


import statistics

nums = [2, 19, 20, 12, 6, 24, 8, 30, 12, 25]

my_sum = sum(nums)
my_min = min(nums)
my_max = max(nums)
my_range = max(nums) - min(nums)
my_mean = my_sum / len(nums)

# Once you finish, print out each value **on its own line** in this format: "sum = " etc.

print(f'''
  sum = {my_sum}
  min = {my_min}
  max = {my_max}
  range = {my_range}
  mean = {my_mean}
''')