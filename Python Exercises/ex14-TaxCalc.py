#Computes tax on an order amount.

amOrder = int(input("What is the order amount? "))
orState = input("What is the state? ")
sTax =  amOrder * 0.055

if orState == "Wi" or orState == "WI" or orState == "wi":
	print("The subtotal is ${:.2f}.\nThe tax is ${:.2f}.\nThe total is ${:.2f}.".format(amOrder, sTax, amOrder + sTax)) 

else:
	print("The total is ${:.2f}".format(amOrder)) 
