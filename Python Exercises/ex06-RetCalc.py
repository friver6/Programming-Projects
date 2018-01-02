#Calculates retirement year according to a certain input.

import datetime

now = datetime.datetime.now()
cAge = input("What is your current age? ")
rAge = input("At what age would you like to retire? ")

yLeft = int(rAge) - int(cAge)
cYear = now.year
rYear = yLeft + cYear

print("You have {} years left until you can retire. It's {}, so you can retire in {}.".format(yLeft, cYear, rYear))
