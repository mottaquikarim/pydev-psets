"""
Basic List Operations II
"""

# Declare a list with 5 names, and print out the length of that list.
names = ['Alana', 'Christen', 'Priya', 'Raina', 'Stacey']
print(names, '\n')

# Print the 3rd name on the list
print('2nd name:', names[2])


# Delete the first name on the list
removed = names.pop(0)
print(f'Pop: {removed} \n')


# Re-add the name you deleted to the end of the list
names.append(removed)
print(names, '\n')

# Replace the 2nd name on the list with a new name.
names.insert(1, 'Natasha')
print(names, '\n')

# Add 3 new names to the end of the list.
names.extend(['Christen', 'Anvesh', 'Taqqui'])
print(names)