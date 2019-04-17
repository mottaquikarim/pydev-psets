"""
Function Basics II - Arguments
"""

# Write a and call function called "names" that separately intakes a person's first name and a person's last name. It should concatenate the names and return the person's full name.

def names(first,last):
	full_name = first + ' ' + last
	return full_name

full_name = names('Taq','Karim')
print(full_name) # Taq Karim