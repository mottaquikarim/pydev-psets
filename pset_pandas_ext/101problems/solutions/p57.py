"""
57. How to reverse the rows of a dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Reverse all the rows of dataframe df.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.arange(25).reshape(5, -1))
"""

# Input
df = pd.DataFrame(np.arange(25).reshape(5, -1))

# Solution 1
df.iloc[::-1, :]

# Solution 2
print(df.loc[df.index[::-1], :])