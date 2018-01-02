#Displays number of slices per person, and if there are any leftovers.

numPeople = input("How many people? ")
numPizzas = input("How many pizzas do you have? ")

slicesPizza = 8
slicesPerPerson = slicesPizza * int(numPizzas) / int(numPeople)
leftovers = slicesPizza * int(numPizzas) % int(numPeople)

print("{} people with {} pizzas\nEach person gets {} pieces of pizza.\nThere are {} leftover pieces.".format(numPeople, numPizzas, round(slicesPerPerson), leftovers))


