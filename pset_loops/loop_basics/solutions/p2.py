"""
Lists with Duplicates - SOLUTION
"""

# First remove dups from a

# then merge b without adding dups

a = [2, 4, 10, 20, 5, 2, 20, 4]
b = [13, 2, 25, 20, 4, 8]

x = []

print(a)

for i in a:
    if i not in x:
        x.append(i)

a = x
print(a)

for i in b:
    if i not in a:
        a.append(i)

print(a)