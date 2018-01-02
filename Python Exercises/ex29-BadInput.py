#Calculates how many years it will take to double an investment.

import math

years = 0
rateRet = 0
usrInput = ""

while True:
	usrInput = input("What is the rate of return? ")
	if (not usrInput.isnumeric() and not usrInput.replace(".", "", 1).isdigit()) or (usrInput == "0"): #Traps invalid input.
		print("Sorry. That's not a valid input.")
	else:
		rateRet = float(usrInput)
		years = math.ceil(72 / rateRet)
		print("It will take {} years to double your initial investment.".format(years))
		break

