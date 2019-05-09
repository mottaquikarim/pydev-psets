"""
14. How to extract items at given positions from a series
"""
"""
Difficulty Level: L1
"""
"""
From ser, extract the items at positions in list pos.
"""
"""
Input
"""
"""
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
"""

# Input
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

# Solution
ser.take(pos)