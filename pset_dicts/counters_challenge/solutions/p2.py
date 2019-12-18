"""
Summing Dict Values - SOLUTION
"""

# Two Kindergarten teachers poll their classes for what fruit they want to eat for snacktime tomorrow. Only one of them is going shopping, so she needs to know how many of each fruit she needs to buy in total. Tally these up and assign them to the "shopping_list" dict.

# Two Kindergarten teachers poll their classes for what fruit they want to eat for snacktime tomorrow. 
# Only one of them is going shopping, so she needs to know how many of each fruit 
# she needs to buy in total. Tally these up and assign them to the "shopping_list" dict.
# Try this with and without the Counter module.


from collections import Counter

poll1 = {'apples': 8, 'bananas': 12}
poll2 = {'apples': 6, 'bananas': 6, 'clementines': 8}

shopping_list = Counter(poll1) + Counter(poll2)
shopping_list = dict(shopping_list)
print(shopping_list)


"""
OR

poll1 = {'apples': 8, 'bananas': 12}
poll2 = {'apples': 6, 'bananas': 6, 'clementines': 8}

### shopping_list = 

apples = poll1['apples'] + poll2['apples']
bananas = poll1['bananas'] + poll2['bananas']


shopping_list = {
'apples': apples,
'bananas': bananas,
'clementines': poll2['clementines']
}

print(shopping_list)
"""
