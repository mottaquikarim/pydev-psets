"""
16. How to get the positions of items of series A in another series B?
"""
"""
Difficulty Level: L2
"""
"""
Get the positions of items of ser2 in ser1 as a list.
"""
"""
Input
"""
"""
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
"""

# Input
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

# Solution 1
[np.where(i == ser1)[0].tolist()[0] for i in ser2]

# Solution 2
[pd.Index(ser1).get_loc(i) for i in ser2]