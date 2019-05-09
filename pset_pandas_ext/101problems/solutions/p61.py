"""
62. How to create a column containing the minimum by maximum of each row?
"""
"""
Difficulty Level: L2
"""
"""
Compute the minimum-by-maximum for every row of df.
"""
"""
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
"""

# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution 1
min_by_max = df.apply(lambda x: np.min(x)/np.max(x), axis=1)

# Solution 2
min_by_max = np.min(df, axis=1)/np.max(df, axis=1)