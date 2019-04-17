"""
Function Basics V - Indeterminate Arguments
"""

# Write a and call a function called "high_low" that takes 3 numbers and returns the highest and lowest ones.

def high_low(*nums):
  group = list(nums)
  length = len(group)

  for i in group:
    if not isinstance(i,int):
      return 'Error: ', 'Please enter only individual integers.'
    else:
      continue

  sorted = group.sort()
  
  high = f'The highest number is {group[length-1]}, and'
  low = f'the lowest number is {group[0]}.'

  return high, low

x = high_low(5, 13, 10, 7)
high, low = x
print(high,low)

y = high_low(15, 4, 8, 21, 11)
high, low = y
print(high,low)

z = high_low(15, [21, 3], 6, 11)
high, low = z
print(high,low)