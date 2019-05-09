"""
48. How to format all the values in a dataframe as percentages?
"""
"""
Difficulty Level: L2
"""
"""
Format the values in column 'random' of df as percentages.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.random(4), columns=['random'])
df
#>      random
#> 0    .689723
#> 1    .957224
#> 2    .159157
#> 3    .21082
"""
"""
Desired Output
"""
"""
#>      random
#> 0    68.97%
#> 1    95.72%
#> 2    15.91%
#> 3    2.10%
"""
