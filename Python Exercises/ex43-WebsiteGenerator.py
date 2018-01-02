import os, os.path
	
def inputVal(pageTitle, sdName, incMSG):
	while True:
		usrChoice = input(incMSG)

		if usrChoice == "Yes" or usrChoice == "Y":
			if not os.path.exists("./{}/{}".format(pageTitle, sdName)):
				os.makedirs("./{}/{}".format(pageTitle, sdName))
				print("Created ./awesomeco/{}".format(sdName))
				break
			else:
				print("{} subdirectory already exists.".format(sdName))
				break
		elif usrChoice == "No" or usrChoice == "N":
			break
		else:
			print("Invalid input.")
			continue

siteName = input("Site name: ")
siteAuthor = input("Author: ")
prompts = ["Do you want a folder for Javascript? ", "Do yo want a folder for CSS? "]

inputVal(siteName, "js", prompts[0])
inputVal(siteName, "css", prompts[1])

with open("index.html", "w") as f:
	f.write("<html><head>")
	f.write("<title>{}</title>".format(siteName))			
	f.write("<meta name=\"author\" content=\"{}\">".format(siteAuthor))
	f.write("</head></html")


	


