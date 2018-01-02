#Generates mult. tables for the numbers 0 through 12.

for i in range(0,13):
	for j in range(0,13):
		print("{} x {} = {}".format(i, j, (i*j)))


