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

# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution Q1
out1 = df.apply(lambda x: ((x - x.mean())/x.std()).round(2))
print('Solution Q1\n',out1)

# Solution Q2
out2 = df.apply(lambda x: ((x.max() - x)/(x.max() - x.min())).round(2))
print('Solution Q2\n', out2)  