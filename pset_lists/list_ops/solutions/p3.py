"""
Math Operations
"""

# A) Save a list with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`. Use this variable for all the problems in this PSET.

numbers = [2, 4, 6, 8]
print('A)', numbers)

# B) Print the max of `numbers`.
print('B)', max(numbers)) # 8


# C) Pop the last element in `numbers` off; re-insert it at index `2` and print the resultant list.
removed = numbers.pop()
numbers.insert(2, removed)
print('C)', numbers) # [2, 4, 8, 6]


# D) Pop the second number in `numbers` off.
print('D)', numbers.pop(1)) # 4


# E) Append `3` to `numbers`.
numbers.append(3)
print('E)', numbers) # [2, 8, 6, 3]


# F) Print out the average number.
avg = sum(numbers) / len(numbers)
print('F)', avg) # 4.75