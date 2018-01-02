#Calculates blood alcohol content based on a formula.

adr = 0 #alcohol distribution ratio
usrGender = input("Enter gender: ")

if usrGender == "M" or usrGender == "m" or usrGender == "male" or usrGender == "Male":
	adr = 0.73
elif usrGender == "F" or usrGender == "f" or usrGender == "female" or usrGender == "Female":
	adr = 0.66
else:
	print("Invalid input.")
	raise SystemExit

amAlc = float(input("Enter amount of alcohol consumed (in oz.): "))
usrWt = float(input("Enter your weight (in pounds): "))
ldHours = float(input("Enter hours since last drink: "))

usrBAC = ((amAlc * 5.14) / (usrWt * adr)) - (0.015 * ldHours)

if usrBAC < 0.08:
	print("Your BAC is {}\nIt is legal for you to drive.".format(usrBAC))
else:
	print("Your BAC is {}\nIt is not legal for you to drive.".format(usrBAC))
