#Picks a winner randomly from a list of contestants.

import random

contestList = []
usrInput = ""

while True:
	usrInput = input("Enter a name: ")
	if not usrInput and not contestList:
		print("No contestants entered.")
		break

	elif not usrInput and contestList:
		print("The winner is...{}.".format(random.choice(contestList)))
		break

	elif usrInput.isalpha():
		contestList.append(usrInput)
		continue

	else:
		print("Invalid input. Try again.")
		continue
