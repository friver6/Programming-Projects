#Pulls data from Open Notify API to show how many people are currently in space.

import requests

desData = requests.get("http://api.open-notify.org/astros.json")
peopleSpace = desData.json() #converts requests object to json format

print("There are {} people in space right now: \n".format(peopleSpace["number"]))

pSpace = peopleSpace["people"]

print("{:<18} | {:<4}".format("Name", "Craft")) 
print("-------------------|------")

for person in pSpace:
	print("{:<18} | {:<4}".format(person['name'], person['craft']))


