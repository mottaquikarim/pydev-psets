"""
53. How to get the last n rows of a dataframe with row sum > 100?
"""
"""
Difficulty Level: L2
"""
"""
Get the last two rows of df whose row sum is greater than 100.
"""
"""
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
"""

# Input
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# Solution
# print row sums
rowsums = df.apply(np.sum, axis=1)

# last two rows with row sum greater than 100
last_two_rows = df.iloc[np.where(rowsums > 100)[0][-2:], :]