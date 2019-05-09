"""
8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
"""
"""
Difficuty Level: L2
"""
"""
Compute the minimum, 25th percentile, median, 75th, and maximum of ser.
"""
"""
Input
"""
"""
ser = pd.Series(np.random.normal(10, 5, 25))
"""

# Input
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))

# Solution
np.percentile(ser, q=[0, 25, 50, 75, 100])