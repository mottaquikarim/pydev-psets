"""
Basic Dict Operations - SOLUTION
"""

"""
Basic Dict Concepts
"""

# A) Declare an empty dict as d1.
d1 = {}


# B) Create a dict called d2 containing the first and last names below:
# Anthony Paollelo, Ping Qiao, Enrique Alvarez, Arjun Dhir 
d2 = {
	'Anthony': 'Paollelo',
	'Ping': 'Qiao',
	'Enrique': 'Alvarez',
	'Arjun': 'Dhir'
}

print('B)\n', d2)
"""
d2 = {
	'Anthony': 'Paollelo',
	'Ping': 'Qiao',
	'Enrique': 'Alvarez',
	'Arjun': 'Dhir',
}
"""



# C) Add Allison Zhang person to d2.
d2.update({'Allison': 'Zhang'})
print('C)\n', d2)

# OR d2['Allison'] = 'Zhang'

"""
d2 = {
	'Anthony': 'Paollelo',
	'Ping': 'Qiao',
	'Enrique': 'Alvarez',
	'Arjun': 'Dhir',
	'Allison': 'Zhang'
}
"""


# D) How many people are now in d2? Print out all their *first* names in the vars below.
num_people = len(d2)
print('D)\n', num_people)

first_names = d2.keys()
print(first_names)



# E) Delete a random person from d2 and print his/her name in the var below.
x = d2.popitem()
print('E)\n', x)



# F) Re-add the name you deleted to the end of d2.
d2.update({x})
print('F)\n', d2)

