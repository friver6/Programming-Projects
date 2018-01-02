#Prompts for five numbers and computes the total.

total = 0
numInput = 0
usrInput = ""


for i in range(0,5):
	usrInput = input("Enter a number: ")
	if usrInput.isdecimal():
		numInput = int(usrInput)
		total += numInput

print("The total is {}.".format(total))
