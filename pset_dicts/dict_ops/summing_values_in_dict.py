"""
Summing Dict Values
"""


# Combine the below dictionaries in dict3. The new dict should contain the same three keys, where their values equal the sum of the values of that key in the original dict.
# ^ should put this in context so it's less confusing. like two polls... and you want to know the total counts from both.

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
a = Counter(d1)
b = Counter(d2)
print(a, '\n', '\n', b, '\n', '\n', d)