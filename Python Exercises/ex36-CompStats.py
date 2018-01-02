#Prints the mean, minimum, maximum, and standard deviation of prompted response times.

import statistics

#Formatted output to display list in one line without brackets.
def printedStats(usrList):
	print("\nNumbers: {}".format(', '.join(map(str, usrList)))) 
	print("The average is {}.".format(statistics.mean(usrList)))
	print("The minimum is {}.".format(min(usrList)))
	print("The maximum is {}.".format(max(usrList)))
	print("The standard deviation is {:.2f}.\n".format(statistics.pstdev(usrList)))

inputNums = []
usrInput = ""

while True:
	usrInput = input("Enter a number: ")
	if usrInput.isdecimal():
		inputNums.append(int(usrInput))
		continue
	elif usrInput == "done":
		if not inputNums:
			print("No available numbers to perform calculations.")
			quit()
		else:	
			break
	else:
		print("Invalid input.")
		continue

printedStats(inputNums)
