#Converts between Fahrenheit and Celsius and vice-versa.

print("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\n")
usrChoice = input("Your choice: ")

if usrChoice == "C" or usrChoice == "c":
	usrTemp = float(input("Please enter the temperature in Fahrenheit: "))
	convTemp = (usrTemp-32) * (5/9)
	print("The temperature in Celsius is {:.2f}.".format(convTemp))

elif usrChoice == "F" or usrChoice == "f":
	usrTemp = float(input("Please enter the temperature in Celsius: "))
	convTemp = (usrTemp * (9/5)) + 32
	print("The temperature in Fahrenheit is {:.2f}.".format(convTemp))

else:
	print("Invalid input.")
	raise SystemExit

