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

# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))
df

# Solution
abs_corrmat = np.abs(df.corr())
max_corr = abs_corrmat.apply(lambda x: sorted(x)[-2])
print('Maximum Correlation possible for each column: ', np.round(max_corr.tolist(), 2))