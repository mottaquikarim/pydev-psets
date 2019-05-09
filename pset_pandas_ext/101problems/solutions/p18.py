"""
18. How to convert the first character of each element in a series to uppercase?
"""
"""
Difficulty Level: L2
"""
"""
Change the first character of each word to upper case in each word of ser.
"""
"""
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
"""

# Input
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

# Solution 1
ser.map(lambda x: x.title())

# Solution 2
ser.map(lambda x: x[0].upper() + x[1:])

# Solution 3
pd.Series([i.title() for i in ser])