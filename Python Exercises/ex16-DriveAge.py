#Program to determine if user can drive according to his or her age.

drivAge = 16

userAge = int(input("What is your age? "))

if userAge <= 0:
	print("Please enter a valid age.")
elif userAge > 0 and userAge < drivAge:
	print("You are not old enough to legally drive.")
else:
	print("You are allowed to drive.")
