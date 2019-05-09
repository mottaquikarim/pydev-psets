"""
11. How to bin a numeric series to 10 groups of equal size?
"""
"""
Difficulty Level: L2
"""
"""
Bin the series ser into 10 equal deciles and replace the values with the bin name.
"""
"""
Input
"""
"""
ser = pd.Series(np.random.random(20))
"""
"""
Desired Output
"""
"""
# First 5 items
0    7th
1    9th
2    7th
3    3rd
4    8th
dtype: category
Categories (10, object): [1st < 2nd < 3rd < 4th ... 7th < 8th < 9th < 10th]
"""

# Input
ser = pd.Series(np.random.random(20))
print(ser.head())

# Solution
pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1], 
        labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head()