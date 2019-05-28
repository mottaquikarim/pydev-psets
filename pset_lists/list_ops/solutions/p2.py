"""
Basic List Operations II
"""

# A) Declare a list with 5 names, and print out the length of that list.
names = ['Alana', 'Christen', 'Priya', 'Raina', 'Stacey']
print('A)', names)

# B) Print the 3rd name on the list
print('B)', names[2]) # Priya


# C) Delete the first name on the list
removed = names.pop(0)
print('C)', removed) # Alana
print(names) # ['Christen', 'Priya', 'Raina', 'Stacey']


# D) Re-add the name you deleted to the end of the list
names.append(removed)
print('D)', names) # ['Christen', 'Priya', 'Raina', 'Stacey', 'Alana']

# E) Replace the 2nd name on the list with a new name.
names.insert(1, 'Natasha')
print('E)', names) # ['Christen', 'Natasha', 'Priya', 'Raina', 'Stacey', 'Alana']

# F) Add 3 new names to the end of the list.
names.extend(['Christen', 'Anvesh', 'Taqqui'])
print('F)', names) # ['Christen', 'Natasha', 'Priya', 'Raina', 'Stacey', 'Alana', 'Christen', 'Anvesh', 'Taqqui']