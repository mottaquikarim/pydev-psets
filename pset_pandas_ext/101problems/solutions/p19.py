"""
19. How to calculate the number of characters in each word in a series?
"""
"""
Difficulty Level: L2
"""
"""
Input
"""
"""
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
"""

# Input
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

# Solution
ser.map(lambda x: len(x))