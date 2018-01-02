#Computes the value of an investment compounded over time.

amPrinc = float(input("What is the principal amount? "))
intRate = float(input("What is the rate? "))
numYears = int(input("What is the number of years? "))
numComp = int(input("What is the number of times the interest in compounded per year? "))

invTotal = amPrinc * pow((1 + ((intRate/100)/numComp)), (numComp * numYears))

print("${:.2f} invested at {}% for {} years compounded {} times per year is ${:.2f}.".format(amPrinc, intRate, numYears, numComp, round(invTotal, 2)))
