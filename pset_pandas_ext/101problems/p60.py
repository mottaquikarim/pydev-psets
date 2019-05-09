"""
61. How to know the maximum possible correlation value of each column against other columns?
"""
"""
Difficulty Level: L2
"""
"""
Compute maximum possible absolute correlation value of each column against other columns in df.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))
"""
