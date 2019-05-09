"""
56. How to swap two rows of a dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Swap rows 1 and 2 in df.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.arange(25).reshape(5, -1))
"""

# Input
df = pd.DataFrame(np.arange(25).reshape(5, -1))

# Solution
def swap_rows(df, i1, i2):
    a, b = df.iloc[i1, :].copy(), df.iloc[i2, :].copy()
    df.iloc[i1, :], df.iloc[i2, :] = b, a
    return df

print(swap_rows(df, 1, 2))