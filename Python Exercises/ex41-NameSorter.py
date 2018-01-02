#Reads list of names, sorts it, and then prints it to a file.

nameList = []
usrInput = ""

while True:
	usrInput = input("Enter the name (last, first): ")
	if usrInput == "done" or usrInput == "Done":
		if not nameList:
			print("No names entered.")
			quit()
		else:
			break
	else:
		nameList.append(usrInput.split(", "))
		continue
print(nameList)

nameList.sort(key=lambda x: x[0])

print(nameList)

with open("nameFile.txt", "w") as f:
	f.write("Total of {} names\n".format(len(nameList)))
	f.write("-----------------\n")
	for person in nameList:
		f.write("{}, {}\n".format(person[0], person[1]))
