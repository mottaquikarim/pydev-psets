"""
58. How to create one-hot encodings of a categorical variable (dummy variables)?
"""
"""
Difficulty Level: L2
"""
"""
Get one-hot encodings for column 'a' in the dataframe df and append it as columns.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
    a   b   c   d   e
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24
"""
"""
Output
"""
"""
   0  5  10  15  20   b   c   d   e
0  1  0   0   0   0   1   2   3   4
1  0  1   0   0   0   6   7   8   9
2  0  0   1   0   0  11  12  13  14
3  0  0   0   1   0  16  17  18  19
4  0  0   0   0   1  21  22  23  24
"""
