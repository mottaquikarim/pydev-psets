"""
68. How to get the n’th largest value of a column when grouped by another column?
"""
"""
Difficulty Level: L2
"""
"""
In df, find the second largest value of 'taste' for 'banana'
"""
"""
Input
"""
"""
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
"""
"""
               
"""

# Input
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'taste': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})

print(df)

# Solution
df_grpd = df['taste'].groupby(df.fruit)
df_grpd.get_group('banana').sort_values().iloc[-2]