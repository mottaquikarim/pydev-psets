"""
69. How to compute grouped mean on pandas dataframe and keep the grouped column as another column (not index)?
"""
"""
Difficulty Level: L1
"""
"""
In df, Compute the mean price of every fruit, while keeping the fruit as another column instead of an index.
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
