#Filters even values of a prompted list of numbers.

numList = input("Enter a list of numbers, separated by spaces: ")
fvalues = ""

for i in numList:
	if i.isdigit() and (int(i) % 2 == 0):
		fvalues +=  i

print("The even numbers are {}.".format(" ".join(fvalues)))

