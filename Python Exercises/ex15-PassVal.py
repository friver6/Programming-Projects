#Validates user login credentials with the use of dictionaries.

import getpass

user = {"fabian" : "abc$123"}

username = input("What is the username? ")

if username in user.keys():
	expected_pass = user[username]
	givenpass = getpass.getpass("What is the password? ")
	if givenpass == expected_pass:
		print("Welcome!")
	else:
		print("Wrong password.")

else:
	print("No user named {}.".format(username))

