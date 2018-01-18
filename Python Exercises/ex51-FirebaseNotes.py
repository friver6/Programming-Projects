# Simple command-line application to save and show
# notes using the Firebase service.

import requests
import datetime
import ex51_config

now = datetime.datetime.now()
sDate = now.strftime("%Y-%m-%d")

while True:
	usrInput = input()
	if (usrInput[0:13] == "mynotes new "):
		noteVar = sDate + " - " + usr[13:]
		dbData = request.post("https://sampproject-1deca.firebaseio.com/Fabian/note.json?access_token=access_token")
		continue
		
	elif(usrInput[0:13] == "mynotes show"):
		dbData2 = request.get("https://sampproject-1deca.firebaseio.com/Fabian/note.json")
		break
	
	else:
		print("Invalid input")
		continue

	
		
