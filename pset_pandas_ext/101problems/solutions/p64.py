"""
65. How to compute the correlation of each row with the suceeding row?
"""
"""
Difficulty Level: L2
"""
"""
Compute the correlation of each row of df with its succeeding row.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
"""

# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution
[df.iloc[i].corr(df.iloc[i+1]).round(2) for i in range(df.shape[0])[:-1]]