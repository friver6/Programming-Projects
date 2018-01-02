#Calculates BMI using a person's weight and height.

usrHeight = float(input("Enter height in inches: "))
usrWeight = float(input("Enter weight in pounds: "))

usrBMI = (usrWeight/(usrHeight * usrHeight)) * 703

if usrBMI < 18.5:
	print("Your BMI is {:.2f}.\nYou are underweight. You should see your doctor.".format(usrBMI))

elif  usrBMI >= 18.5 and usrBMI <= 25:
	print("Your BMI is {:.2f}.\nYou are within the ideal weight range.".format(usrBMI))

else:
	print("Your BMI is {:.2f}.\nYou are overweight. You should see your doctor.".format(usrBMI))
