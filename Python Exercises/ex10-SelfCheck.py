#Simple check-out system that prompts for prices and quantities of three items.

itemList = []
quant = 0
price = 0
subtotal = 0
total = 0
tax = 0

#Using a list of lists to store the values.
for i in range(1,4):
	price = float(input("Enter the price of item " + str(i) + ": "))
	quant = int(input("Enter the quantity of item " + str(i) + ": "))
	item = [price, quant]
	itemList.append(item)

print(itemList)

#Accessing each sublist's values to obtain subtotal.
for list in itemList:
	accVal = list[0] * list[1]
	subtotal += accVal

tax = 0.055 * subtotal
total = tax + subtotal

print("\nSubtotal: ${:.2f}\nTax: ${}\nTotal: ${}\n".format(subtotal, tax, total))

