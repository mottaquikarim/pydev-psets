"""
24. How to filter words that contain atleast 2 vowels from a series?
"""
"""
Difficiulty Level: L3
"""
"""
From ser, extract words that contain atleast 2 vowels.
"""
"""
Input
"""
"""
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
"""
"""
Desired Output
"""
"""
0     Apple
1    Orange
4     Money
dtype: object
"""

# Input
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

# Solution
from collections import Counter
mask = ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
ser[mask]