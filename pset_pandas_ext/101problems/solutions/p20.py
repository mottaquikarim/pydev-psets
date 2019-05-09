"""
20. How to compute difference of differences between consequtive numbers of a series?
"""
"""
Difficulty Level: L1
"""
"""
Difference of differences between the consequtive numbers of ser.
"""
"""
Input
"""
"""
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
"""
"""
Desired Output
"""
"""
[nan, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 8.0]
[nan, nan, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0]
"""

# Input
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

# Solution
print(ser.diff().tolist())
print(ser.diff().diff().tolist())