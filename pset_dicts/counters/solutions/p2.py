"""
Summing Dict Values - SOLUTION
"""

shopping_list = Counter(poll1) + Counter(poll2)
# print(final_tally) # Counter({'bananas': 18, 'apples': 14, 'clementines': 8})

poll1 = dict(shopping_list)
print(poll1) # {'apples': 14, 'bananas': 18, 'clementines': 8}