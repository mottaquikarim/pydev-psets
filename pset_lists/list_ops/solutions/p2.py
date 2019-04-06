"""
Core Statistics Calculations - SOLUTION
"""

import statistics

nums = [2, 19, 20, 12, 6, 24, 8, 30, 12, 25]

my_sum = sum(nums)
my_min = min(nums)
my_max = max(nums)
my_range = max(nums) - min(nums)
my_mean = my_sum / len(nums)
my_median = statistics.median_grouped(nums)
my_mode = statistics.mode(nums)
my_variance = statistics.variance(nums, my_mean)
my_stdev = statistics.stdev(nums, my_mean)


print(f'''
  sum = {my_sum}
  min = {my_min}
  max = {my_max}
  range = {my_range}
  mean = {my_mean}
''')

print(f'''
  median = {my_median}
  mode = {my_mode}
  variance = {my_variance}
  standard deviation = {my_stdev}
''')
