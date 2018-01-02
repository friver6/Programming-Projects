#Display number of gallons of paint needed, as a whole number.

import math

lenFeet = input("Enter ceiling length: ")
widFeet = input("Enter ceiling width: ")

galPerFeet = (1/350)
ceilArea = float(lenFeet) * float(widFeet)
numGals = math.ceil(galPerFeet * ceilArea)

print("You will need to purchase {} gallons of paint to cover {} square feet.".format(numGals, round(ceilArea)))


