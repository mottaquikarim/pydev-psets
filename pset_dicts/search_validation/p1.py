"""
Basic Login
"""

# Imagine you work for a movie streaming service. You're in charge of safeguarding user privacy by ensuring the login feature remains secure. For the sake of example only, below is the dict of user login info. Normally, you wouldn't have access to see this unencrypted of course!

users = {
	'person@email.com': 'PassWord',
	'someone@email.com': 'hiitsme',
	'me@email.com': 'myPassword',
	'anyone@email.com': 'IMawesome',
	'guy@email.com': 'pa$$wordz'
	# etc
}


# A user enters the below login info (email and password) for your app. Search your database of user logins to see if this account exists and if the password matches what you have on file. If the login credentials are correct, print "Successful login!". Otherwise, print "The login info you entered does not match any of our records."

current_user = { 'me@email.com': 'myPassword' }