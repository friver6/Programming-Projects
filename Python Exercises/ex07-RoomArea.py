#Calculates the area of a room is feet and meters.

rLength = input("What is the length of the room in feet? ")
rWidth = input("What is the width of the room in feet? ")

convFact = 0.09290304
rArea = float(rLength) * float(rWidth)
area_sm = rArea * convFact

print("You entered dimensions of {} feet by {} feet.\nThe area is \n{} square feet\n{:.3f} square meters".format(rLength, rWidth, round(rArea), area_sm))


