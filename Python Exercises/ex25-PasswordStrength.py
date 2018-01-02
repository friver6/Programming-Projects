#Determines the complexity of a given password based on given rules.

def passwordValidator(incInput):
	ps = ""

	if len(incInput) >= 8 and not incInput.isalnum() and not incInput.isdecimal() and not incInput.isalpha():
		ps = "very strong"
	elif len(incInput) >= 8 and incInput.isalnum() and not incInput.isdecimal() and not incInput.isalpha():
		ps = "strong"
	elif len(incInput) < 8 and incInput.isalpha() and not incInput.isdecimal():
		ps = "weak"
	else:
		ps = "very weak"
	
	printResult(incInput, ps)

def printResult(password, rating):
	print("{} is a {} password.".format(password, rating))

usrPass = input("Enter the password: ")

passwordValidator(usrPass)
