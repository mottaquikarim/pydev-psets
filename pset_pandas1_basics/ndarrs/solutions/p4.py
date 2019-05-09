"""
basic operations
"""

import numpy as np

arr = np.array([1, 2, 5, 3])

# add 1 to every element
a = arr + 1
print("Adding 1 to every element:", a)

# subtract 3 from each element
b = arr - 3
print("Subtracting 3 from each element:", b)

# multiply each element by 10
c = arr * 10
print("Multiplying each element by 10:", c)

# square each element
d = arr ** 2
print("Squaring each element:", d)

# Doubled each element of *original* array
print("Doubled each element of original array:", arr *= 2)
