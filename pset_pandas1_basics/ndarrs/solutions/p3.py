"""
ndarray indexing
"""


import numpy as np
# given this
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# grab first two rows of arr
a = arr[:2]

# grab second and third row of arr
b = arr[1:3]

# grab first two rows of arr and first two columns
c = arr[:2, :2]

# grab elements at indices (0, 3), (1, 2), (2, 1), (3, 0)
d = arr[[0, 1, 2, 3], [3, 2, 1, 0]]


# grab elements > 0
cond = arr > 0  # cond is a boolean array
e = arr[cond]
