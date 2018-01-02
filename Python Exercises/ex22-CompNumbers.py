#Determines the largest number without built-in functions.

fNum = int(input("Enter the first number: "))
sNum = int(input("Enter the second number: "))
tNum = int(input("Enter the third number: "))
largNum = 0

if fNum >= sNum and fNum >= tNum:
	largNum = fNum
elif sNum >= fNum and sNum >= tNum:
	largNum = sNum
else:
	largNum = tNum

print("The largest number is {}.".format(largNum))
