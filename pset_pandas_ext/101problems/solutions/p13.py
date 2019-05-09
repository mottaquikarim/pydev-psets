"""
13. How to find the positions of numbers that are multiples of 3 from a series?
"""
"""
Difficulty Level: L2
"""
"""
Find the positions of numbers that are multiples of 3 from ser.
"""
"""
Input
"""
"""
ser = pd.Series(np.random.randint(1, 10, 7))
"""

# Input
ser = pd.Series(np.random.randint(1, 10, 7))
ser

# Solution
print(ser)
np.argwhere(ser % 3==0)