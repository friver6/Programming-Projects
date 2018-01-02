#Program that prompts for certain information, and verifies the validity of those inputs.
#Wanted to do the problem without the use of regular expressions.

def fnVal(sn):
	nvList = []
	if not sn:
		nvList.append("First name must be filled in.")
	if len(sn) == 1:
		nvList.append("\"{}\" is not the right size. It's too short.".format(sn))
	if sn and not sn.isalpha():
		nvList.append("Numbers are not allowed in first name.")

	return nvList

def lnVal(sn):
	nvList = []
	if not sn:
		nvList.append("Last name must be filled in.")
	if len(sn) == 1:
		nvList.append("\"{}\" is not the right size. It's too short.".format(sn))
	if sn and not sn.isalpha():
		nvList.append("Numbers are not allowed in last name.")

	return nvList

def zipVal(zc):
	zipList = []
	if not zc:
		zipList.append("Zip code must be filled in.")
	if len(zc) != 5:
		zipList.append("Zip code must be 5 characters long.")
	if zc and not zc.isdecimal():
		zipList.append("Zip code must be numeric.")
	
	return zipList

def empVal(ei):
	empList = []
	
	if not ei:
		empList.append("ID must be filled in.")
	if len(ei) != 7 or not ei[:2].isalpha() or ei[2] != "-" or not ei[3:].isdecimal():
		empList.append("{} is not a valid ID.".format(ei))

	return empList

def validateInput(first, last, zipC, eID):
	valInList = []
	valInList = fnVal(first) + lnVal(last) + zipVal(zipC) + empVal(eID)
	if not valInList:
		print("There were no errors found.")
	else:
		for elem in valInList:
			print(elem)

fName = input("Enter the first name: ")
lName = input("Enter the last name: ")
zCode = input("Enter the ZIP code: ")
empID = input("Enter an employee ID: ")

validateInput(fName, lName, zCode, empID)
