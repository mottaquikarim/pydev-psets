"""
38. How to extract the row and column number of a particular cell with given criterion?
"""
"""
Difficulty Level: L1
"""
"""
Input
"""
"""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
"""
"""
Which manufacturer, model and type has the highest Price? What is the row and column number of the cell with the highest Price value?
"""
"""
 
"""

# Input
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Solution
# Get Manufacturer with highest price
df.loc[df.Price == np.max(df.Price), ['Manufacturer', 'Model', 'Type']]

# Get Row and Column number
row, col = np.where(df.values == np.max(df.Price))

# Get the value
df.iat[row[0], col[0]]
df.iloc[row[0], col[0]]

# Alternates
df.at[row[0], 'Price']
df.get_value(row[0], 'Price')

# The difference between `iat` - `iloc` vs `at` - `loc` is:
# `iat` snd `iloc` accepts row and column numbers. 
# Whereas `at` and `loc` accepts index and column names.