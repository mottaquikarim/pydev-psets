"""
basic operations II
"""

import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print("Largest element is:", arr.max())

# minimum element of array
print("Smallest element is:", arr.min())

# maximum element per row
print("Row-wise maximum elements:",
      arr.max(axis=1))

# minimum element per col
print("Column-wise minimum elements:",
      arr.min(axis=0))

# sum of array elements
print("Sum of all array elements:",
      arr.sum())

# cumulative sum along each row
print("Cumulative sum along each row:\n",
      arr.cumsum(axis=1))

c = np.array([[1, 2],
              [3, 4]])
d = np.array([[4, 3],
              [2, 1]])

# add arrays
print("Array sum:\n", c + d)

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", c * d)
