"""
74. How to get the frequency of unique values in the entire dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Get the frequency of unique values in the entire dataframe df.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
"""

# Input
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))

# Solution
pd.value_counts(df.values.ravel())