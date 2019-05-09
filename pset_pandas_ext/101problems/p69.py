"""
70. How to join two dataframes by 2 columns so they have only the common rows?
"""
"""
Difficulty Level: L2
"""
"""
Join dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’.
"""
"""
Input
"""
"""
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})
"""
