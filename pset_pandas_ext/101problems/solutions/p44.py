"""
44. How to select a specific column from a dataframe as a dataframe instead of a series?
"""
"""
Difficulty Level: L2
"""
"""
Get the first column (a) in df as a dataframe (rather than as a Series).
"""
"""
Input
"""
"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
"""

# Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# Solution
type(df[['a']])
type(df.loc[:, ['a']])
type(df.iloc[:, [0]])

# Alternately the following returns a Series
type(df.a)
type(df['a'])
type(df.loc[:, 'a'])
type(df.iloc[:, 1])