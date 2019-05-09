"""
27. How to compute the euclidean distance between two series?
"""
"""
Difficiulty Level: L2
"""
"""
Compute the euclidean distance between series (points) p and q, without using a packaged formula.
"""
"""
Input
"""
"""
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
"""
"""
Desired Output
"""
"""
18.165
"""

# Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Solution 
sum((p - q)**2)**.5

# Solution (using func)
np.linalg.norm(p-q)