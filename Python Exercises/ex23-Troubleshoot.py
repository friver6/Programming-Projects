#Walks the user through troubleshooting issues with a car.
#Used functions to simplify the code.

def firstLevel():
	usrInput = input("Is the car silent when you turn the key? ")

	if usrInput == "Y":
		secInput = input("Are the battery terminals corroded? ")
		if secInput == "Y":
			print("Clean the terminals and try starting again.")
		elif secInput == "N":
			print("Replace cables and try again.")
		else: 
			print("Invalid input.")

	elif usrInput == "N":
		secLevel()

	else:
		print("Invalid input.")

def secLevel():
	usrInput = input("Does the car make a clicking noise? ")
	if usrInput == "Y":
		print("Replace the battery.")
	elif usrInput == "N":
		thirdLevel()
	else:
		print("Invalid input.")

def thirdLevel():
	usrInput = input("Does the car crank up but fail to start? ")
	
	if usrInput == "Y":
		print("Check spark plug connections.")
	elif usrInput == "N":
		fourthLevel()
	else:
		print("Invalid input.")

def fourthLevel():
	usrInput = input("Does the engine start and then die? ")
	if usrInput == "Y":
		secInput = input("Does your car have fuel injection? ")
		if secInput == "Y":
			print("Get it in for service.")
		elif secInput == "N":
			print("Check to ensure the choke is opening and closing.")
		else:
			print("Invalid input.")
	else:
		print("Invalid input.")

firstLevel()
		




