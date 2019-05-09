"""
41. How to count the number of missing values in each column?
"""
"""
Difficulty Level: L2
"""
"""
Count the number of missing values in each column of df. Which column has the maximum number of missing values?
"""
"""
Input
"""
"""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
"""

# Input
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Solution
n_missings_each_col = df.apply(lambda x: x.isnull().sum())
n_missings_each_col.argmax()