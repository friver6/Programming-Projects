#Processes a read data set, and displays the formatted result.

nameList = []

#Reads each line from the text file, strips the newline character, and stores it in a list.
with open("nameSet.txt", "r") as f:
	nameList = [line.strip() for line in f]

#Converts each element of the list into a sublist.
nameList = [x.split(",") for x in nameList]

#Sorts list by salary (in descending order).
nameList.sort(key=lambda x: x[2], reverse=True)

print("\n{:8} {:8} {}".format("First", "Last", "Salary"))
print("------------------------")

for name in nameList:
	print("{:8} {:8} ${}".format(name[0], name[1], name[2]))


