#Searches json file for a given product.

import json

with open("sDoc.json") as json_data:
	a = json.load(json_data)

pname = ""
#extracts the list "value" from the dictionary.
l = a.get('products')
resList = []

while True:
	pname = input("What is the product name? ")
	#searches the list of dictionaries and extracts the results into a new list.
	resList = list(filter(lambda nItem: nItem['name'] == pname, l))
	if not resList:
		print("Sorry, that product was not found in our inventory.")
		continue
	else:
		#turns result back into a dicitonary.
		nD = dict(resList[0])
		print(nD)
		print("Name: {}\nPrice: ${:0.2f}\nQuantity on hand: {}".format(nD['name'], nD['price'], nD['quantity']))
		break
	
		
