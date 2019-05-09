"""
45. How to change the order of columns of a dataframe?
"""
"""
Difficulty Level: L3
"""
"""
Actually 3 questions.
"""
"""
In df, interchange columns 'a' and 'c'.Create a generic function to interchange two columns, without hardcoding column names.Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
"""

# Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# Solution Q1
df[list('cbade')]

# Solution Q2 - No hard coding
def switch_columns(df, col1=None, col2=None):
    colnames = df.columns.tolist()
    i1, i2 = colnames.index(col1), colnames.index(col2)
    colnames[i2], colnames[i1] = colnames[i1], colnames[i2]
    return df[colnames]

df1 = switch_columns(df, 'a', 'c')

# Solution Q3
df[sorted(df.columns)]
# or
df.sort_index(axis=1, ascending=False, inplace=True)