"""
43. How to use apply function on existing columns with global variables as additional arguments?
"""
"""
Difficulty Level: L3
"""
"""
In df, use apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.
"""
"""
Input
"""
"""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
"""
"""
Use Hint from StackOverflow
"""
"""
 
"""

# Input
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Solution
d = {'Min.Price': np.nanmean, 'Max.Price': np.nanmedian}
df[['Min.Price', 'Max.Price']] = df[['Min.Price', 'Max.Price']].apply(lambda x, d: x.fillna(d[x.name](x)), args=(d, ))