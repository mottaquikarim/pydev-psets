"""
26. How to get the mean of a series grouped by another series?
"""
"""
Difficiulty Level: L2
"""
"""
Compute the mean of weights of each fruit.
"""
"""
Input
"""
"""
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weight.tolist())
print(fruit.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']
"""
"""
Desired output
"""
"""
# values can change due to randomness
apple     6.0
banana    4.0
carrot    5.8
dtype: float64
"""
