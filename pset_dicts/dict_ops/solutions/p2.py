"""
Merging Dicts - SOLUTION
"""

# Merge these two dicts without creating a new one.

d1 = {'a': 100, 'b': 200}
d2 = {'c': 300, 'd': 400, 'e': 500}

d1.update(d2)
print(d1)

# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}