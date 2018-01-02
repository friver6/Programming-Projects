#Sorts employee list by last name.

empList = []

numEmps = input("How many employees will be entered? ")

if not numEmps.isdigit():
	print("Invalid input.")
	quit()

#Loop takes care of instances where the date is not given by adding a blank.
for i in range(0, int(numEmps)):
	usrInput = input("Enter information (separated by commas): ")
	usrInput = [x.strip() for x in usrInput.split(",")]	
	while len(usrInput) < 4:
		usrInput.append(" ")

	empList.append(usrInput)

#Sorting statement
empList.sort(key=lambda x: x[1])

print("\nEmployee\t\t| Position\t\t| Separation Date\t")
print("------------------------|-----------------------|--------------------")
for emp in empList:
	print("{} {:<12}\t| {:<18}\t| {:<12}".format(emp[0], emp[1], emp[2], emp[3]))


#The following lets the user search the data set for entries matching a certain string.
usrSearch = input("\nEnter search string: ")

print("\nResults:\nEmployee\t\t| Position\t\t| Separation Date\t")
print("------------------------|-----------------------|--------------------")

for emp in empList:
	for elem in emp:
		if usrSearch in elem:
			print("{} {:<12}\t| {:<18}\t| {:<12}".format(emp[0], emp[1], emp[2], emp[3]))
			break
