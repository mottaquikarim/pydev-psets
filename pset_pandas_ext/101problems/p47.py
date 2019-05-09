"""
47. How to format or suppress scientific notations in a pandas dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
"""
"""
Desired Output
"""
"""
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000
"""
