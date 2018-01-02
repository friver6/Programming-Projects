#Determine how many months it will take to pay off a credit card balance, as in previous examples, formula is given by the author.

import math

def calculateMonthsUntilPaidOff(uB, uAPR, mp):
	dR = (uAPR / 100) / 365
	numMonths = (math.log(1 + ((uB/mp) * (1 - pow((1 + dR), 30))))) / (-30 * (math.log(1 + dR)))
	numMonths = math.ceil(numMonths)
	return numMonths

usrBal = float(input("What is your balance? "))
usrAPR = float(input("What is the APR on the card (as a percent)? "))
mPay = float(input("What is the monthly payment you can make? "))

nm = calculateMonthsUntilPaidOff(usrBal, usrAPR, mPay)

print("It will take you {} months to pay off this card.".format(nm))
