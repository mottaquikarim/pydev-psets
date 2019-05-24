"""
Math Operations
"""

# Save a list with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`. Use this variable for all the problems in this PSET.

numbers = [2, 4, 6, 8]
print(numbers, '\n')

# Print the max of `numbers`.
print(max(numbers), '\n')

# Pop the last element in `numbers` off; re-insert it at index `2`.
removed = numbers.pop()
print(removed)
numbers.insert(2, removed)
print(numbers, '\n')

# Pop the second number in `numbers` off.
print(numbers.pop(1), '\n')


# Append `3` to `numbers`.
numbers.append(3)


# Print out the average number.
avg = sum(numbers) / len(numbers)
print(avg, '\n')


# Print `numbers`.
print(numbers)
