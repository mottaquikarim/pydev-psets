"""
6. How to get the items of series A not present in series B?
"""
"""
Difficulty Level: L2
"""
"""
From ser1 remove items present in ser2.
"""
"""
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
"""

# Input
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser1[~ser1.isin(ser2)]