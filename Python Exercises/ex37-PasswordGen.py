#Generates a secure password.

import random, string

spList = "!@#$%*()_+-=~`':;,./<>?[]\\|"
genWord = []
minLength = int(input("What's the minimum length? "))
spChars = int(input("How many special characters? "))
amNums = int(input("How many numbers? "))

#I used random.sample() to take the specified 
#amount of special chars. or numbers, then
#used it again to fill the generated password
#with letters (lower and upper case).

numPart = random.sample(string.digits, amNums)
spPart = random.sample(spList, spChars)
letLeft = minLength - len(numPart + spPart)
letPart = random.sample(string.ascii_letters, random.randint(letLeft,minLength))
genWord = numPart + spPart + letPart
random.shuffle(genWord)

print("Your password is {}".format(''.join(genWord)))

