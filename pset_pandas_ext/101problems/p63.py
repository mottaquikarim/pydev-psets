"""
64. How to normalize all columns in a dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Normalize all columns of df by subtracting the column mean and divide by standard deviation.Range all columns of df such that the minimum value in each column is 0 and max is 1.
"""
"""
Don’t use external packages like sklearn.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
"""
