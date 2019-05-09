"""
12. How to convert a numpy array to a dataframe of given shape? (L1)
"""
"""
Difficulty Level: L1
"""
"""
Reshape the series ser into a dataframe with 7 rows and 5 columns
"""
"""
Input
"""
"""
ser = pd.Series(np.random.randint(1, 10, 35))
"""

# Input
ser = pd.Series(np.random.randint(1, 10, 35))

# Solution
df = pd.DataFrame(ser.values.reshape(7,5))
print(df)