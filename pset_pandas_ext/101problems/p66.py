"""
67. How to get the particular group of a groupby dataframe by key?
"""
"""
Difficulty Level: L2
"""
"""
This is a question related to understanding of grouped dataframe. From df_grouped, get the group belonging to 'apple' as a dataframe.
"""
"""
Input
"""
"""
df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])
"""
"""
# Input
df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])

# Solution 1
df_grouped.get_group('apple')

# Solution 2
for i, dff in df_grouped:
    if i == 'apple':
        print(dff)
"""
"""
    col1      col2  col3
0  apple  0.673434     7
3  apple  0.182348    14
6  apple  0.050457     3
"""
