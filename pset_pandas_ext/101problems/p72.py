"""
73. How to create lags and leads of a column in a dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Create two new columns in df, one of which is a lag1 (shift column a down by 1 row) of column ‘a’ and the other is a lead1 (shift column b up by 1 row).
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))

    a   b   c   d
0  66  34  76  47
1  20  86  10  81
2  75  73  51  28
3   1   1   9  83
4  30  47  67   4
"""
"""
Desired Output
"""
"""
    a   b   c   d  a_lag1  b_lead1
0  66  34  76  47     NaN     86.0
1  20  86  10  81    66.0     73.0
2  75  73  51  28    20.0      1.0
3   1   1   9  83    75.0     47.0
4  30  47  67   4     1.0      NaN
"""
