"""
Basic Dict Operations - SOLUTION
"""

d1 = {}

d2 = {
	'Anthony': 'Paollelo',
	'Ping': 'Qiao',
	'Enrique': 'Alvarez',
	'Arjun': 'Dhir'
}


d2.update('Allison', 'Zhang')
print(d2)
"""
d2 = {
	'Anthony': 'Paollelo',
	'Ping': 'Qiao',
	'Enrique': 'Alvarez',
	'Arjun': 'Dhir',
	'Allison': 'Zhang'
}
"""

# OR

d2['Allison', 'Zhang']

num_people = len(d2)
print(num_people)

first_names = d2.keys()
print(first_names)

x = d2.popitem()

d2.update(x)


