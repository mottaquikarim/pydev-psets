"""
Ordering Random Numbers
"""

# Create a list of 6 randomly generated numbers called numbers and sort it in descending order.

from random import randint

numbers = []
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))
numbers.append(randint(6, 100))

print(f'Unsorted: {numbers}\n')


numbers.sort(reverse = True)
# OR... numbers = sorted(numbers, reverse = True)

print(f'Sorted: {numbers}\n')