"""
17. How to compute the mean squared error on a truth and predicted series?
"""
"""
Difficulty Level: L2
"""
"""
Compute the mean squared error of truth and pred series.
"""
"""
Input
"""
"""
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
"""

# Input
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

# Solution
np.mean((truth-pred)**2)