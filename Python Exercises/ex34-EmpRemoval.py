#Contains a list of employees, and removes the one chosen by the user.

def empDisplay(usrList):
	print("\nThere are {} employees: ".format(len(usrList)))
	for emp in usrList:
		print(emp)

empList = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

empDisplay(empList)

empChosen = input("\nEnter an employee name to remove: ")

if empChosen in empList:
	empList.remove(empChosen)
	empDisplay(empList)

else:
	print("\nThis person is not in the list.")
