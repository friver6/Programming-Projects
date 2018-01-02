#Computes simple interest.

amPrinc = float(input("Enter the principal: "))
intRate = float(input("Enter the rate of interest: "))
numYears = int(input("Enter the number of years: "))

intRate /= 100
invTotal = amPrinc * (1 + (intRate * numYears))

#print(invTotal)
print("After {} years at {}%, the investment will be worth ${:.2f}.".format(numYears, (intRate * 100), round(invTotal)))
