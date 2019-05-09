"""
15. How to stack two series vertically and horizontally ?
"""
"""
Difficulty Level: L1
"""
"""
Stack ser1 and ser2 vertically and horizontally (to form a dataframe).
"""
"""
Input
"""
"""
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
"""

# Input
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# Output
# Vertical
ser1.append(ser2)

# Horizontal
df = pd.concat([ser1, ser2], axis=1)
print(df)