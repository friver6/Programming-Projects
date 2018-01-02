#Guess a number game, with three levels of difficulty.

from random import randint

def levelVal():
	lvl = ""
	genNum = 0
	while True:
		lvl = input("Pick a difficulty (1, 2, or 3): ")
		if lvl.isdecimal() and (int(lvl) >= 1 and int(lvl) <= 3):
			lvl = int(lvl)
			break
		else:
			print("Invalid input.")
			continue
	
	if lvl == 1:
		genNum = randint(0, 11)
	elif lvl == 2:
		genNum = randint(0, 101)
	else:
		genNum = randint(0, 1001)

	return genNum

def gameEngine():
	numGuesses = 0
	playAgain = ""
	gameChoice = levelVal()
	usrGuess = input("I have my number. What's your guess? ")

	while True:
		if usrGuess.isdecimal():
			if int(usrGuess) == gameChoice:
				numGuesses += 1
				print("{} is right! You got it in {} guesses".format(usrGuess, numGuesses))
				break
			elif int(usrGuess) > gameChoice:
				numGuesses += 1
				usrGuess = input("Too high. Guess again: ")
				continue
			else:
				numGuesses += 1
				usrGuess = input("Too low. Guess again: ")
				continue
		else:
			numGuesses += 1
			usrGuess = input("Invalid input. Guess again: ")
			continue

	playAgain = input("Play again? ")

	while True:
		if playAgain == "Y" or playAgain == "yes":
			gameEngine()

		elif playAgain == "N" or playAgain == "no":
			quit()
		else:
			playAgain = input("Invalid input. Play again? ")
			continue
		

print("Let's play Guess the Number.")

gameEngine()


