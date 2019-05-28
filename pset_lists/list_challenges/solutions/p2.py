"""
CHALLENGE - Core Statistics Calculations
"""

# Given the sample below, find the median, mode, variance, and standard deviation of this sample. Print them out separately, but in the same format as before.
	# my_median = 
	# my_mode = 
	# my_variance = 
	# my_sd = 


import statistics

sample = [6, 19, 20, 12, 6, 24, 8, 30, 28, 25]

my_mean = sum(sample) / len(sample)
my_median = statistics.median_grouped(sample)
my_mode = statistics.mode(sample)
my_variance = statistics.variance(sample, my_mean)
my_stdev = statistics.stdev(sample, my_mean)


# Once you finish, print out each value **on its own line** in this format: "median = " etc.

print(f'''
  median = {my_median}
  mode = {my_mode}
  variance = {my_variance}
  standard deviation = {my_stdev}
''')