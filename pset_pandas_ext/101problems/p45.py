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
