"""
54. How to find and cap outliers from a series or dataframe column?
"""
"""
Difficulty Level: L2
"""
"""
Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 5th and 95th %ile value.
"""
"""
Input
"""
"""
ser = pd.Series(np.logspace(-2, 2, 30))
"""
