"""
Basic Login Search - SOLUTION
"""

users = {
	'person@email.com': 'PassWord',
	'someone@email.com': 'p@$$w0rd',
	'me@email.com': 'myPassword',
	'anyone@email.com': 'p@ssw0rd',
	'guy@email.com': 'pa$$word'
	# etc
}

# A user enters the below login info (email and password) for your app. Search your database of user logins to see if this account exists and if the password matches what you have on file. If the login credentials are correct, print "Successful login!". Otherwise, print "The login info you entered does not match any of our records."


current_user = { 'me@email.com': 'myPassword' }
name = list(current_user.keys())
name = name[0]
pw = list(current_user.values())
pw = pw[0]

if name in users.keys() and users[name] is pw:
	print('Successful login!')
else:
	print('The login info you entered does not match any of our records.')