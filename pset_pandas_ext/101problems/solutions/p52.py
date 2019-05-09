"""
52. How to find the position of the nth largest value greater than a given value?
"""
"""
Difficulty Level: L2
"""
"""
In ser, find the position of the 2nd largest value greater than the mean.
"""
"""
Input
"""
"""
ser = pd.Series(np.random.randint(1, 100, 15))
"""

# Input
ser = pd.Series(np.random.randint(1, 100, 15))

# Solution
print('ser: ', ser.tolist(), 'mean: ', round(ser.mean()))
np.argwhere(ser > ser.mean())[1]