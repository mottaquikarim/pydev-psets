"""
55. How to reshape a dataframe to the largest possible square after removing the negative values?
"""
"""
Difficulty Level: L3
"""
"""
Reshape df to the largest possible square with negative values removed. Drop the smallest values if need be. The order of the positive numbers in the result should remain the same as the original.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
"""
