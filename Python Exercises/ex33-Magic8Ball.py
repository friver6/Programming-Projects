import random

answerList = ["Yes", "No", "Maybe", "Ask again later."]
ballAnswer = ""

usrQuestion = input("What's your question? ")

while True:
	if "?" in usrQuestion:
		ballAnswer = random.choice(answerList)
		print(ballAnswer)
		break
	else:
		usrQuestion = input("That was not a question, try again: ")
		continue
