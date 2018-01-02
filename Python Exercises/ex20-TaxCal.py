#Calculates state tax according to state or county.

amOrder = float(input("What is the order amount? "))
usrState = input("What state do you live in? ")
usrCounty = ""
stateTax = 0
total = 0

if usrState == "WI" or usrState == "Wisconsin":
	stateTax = amOrder * 0.05	
	usrCounty == input("What county do you live in? ")
	if usrCounty == "Eau Claire":
		stateTax += 0.005
	elif usrCounty == "Dunn":
		stateTax += 0.004

elif usrState == "IL" or usrState == "Illinois":
	stateTax = amOrder * 0.08

total = amOrder + stateTax

print("The tax is ${:.2f}.\nThe total is ${:.2f}.".format(stateTax, total))
