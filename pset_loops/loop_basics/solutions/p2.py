"""
Lists with Duplicates - SOLUTION
"""

# First remove dups from a

# then merge b without adding dups

a = [2, 4, 10, 20, 5, 2, 20, 4]
b = [13, 2, 25, 20, 4, 8]

print(f'BASE LIST: {a}\n')


# USING A LOOP, remove the duplicate items from list a and print out the updated list.

x = []

for i in a:
    if i not in x:
        x.append(i)

a = x
print(f'Removed Dups: {a}\n')


# SING A LOOP, merge list b into list a without adding any duplicates.

for i in b:
    if i not in a:
        a.append(i)

print(f'Merged: {a}')
