#Uses Karvonen formula to determine the target heart rate based on a range of intensities.

#Catches invalid inputs.
def inputVal(incInput, incPrompt):
	while True:
		incInput = input(incPrompt)
		if incInput.isdigit():
			incInput = int(incInput)
			return incInput
		else:
			print("Invalid Input.")
			continue

usrAge = ""
restPulse = ""
prompts = ["Enter your age: ", "Enter your resting pulse: "]

usrAge = inputVal(usrAge, prompts[0])
restPulse = inputVal(restPulse, prompts[1])

print("\nResting Pulse: {}\tAge: {}".format(restPulse, usrAge))
print("Intensity\t| Rate   ")
print("----------------|---------")

#"i" will be the intensity
for i in range(55, 96, 5):
	karvHR = (((220 - usrAge) - restPulse) * (i/100)) + restPulse
	print("{}%  \t\t| {} bpm".format(i, round(karvHR)))

