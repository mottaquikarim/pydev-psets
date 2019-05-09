"""
63. How to create a column that contains the penultimate value in each row?
"""
"""
Difficulty Level: L2
"""
"""
Create a new column 'penultimate' which has the second largest value of each row of df.
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
out = df.apply(lambda x: x.sort_values().unique()[-2], axis=1)
df['penultimate'] = out
print(df)