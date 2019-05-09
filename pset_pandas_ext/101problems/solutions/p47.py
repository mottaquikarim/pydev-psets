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

# Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])

# Solution 1: Rounding
df.round(4)

# Solution 2: Use apply to change format
df.apply(lambda x: '%.4f' % x, axis=1)
# or
df.applymap(lambda x: '%.4f' % x)

# Solution 3: Use set_option
pd.set_option('display.float_format', lambda x: '%.4f' % x)

# Solution 4: Assign display.float_format
pd.options.display.float_format = '{:.4f}'.format
print(df)

# Reset/undo float formatting
pd.options.display.float_format = None