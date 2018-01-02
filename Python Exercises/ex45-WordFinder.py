#Replaces ocurrences of a certain word into a new text file.

with open("samp1.txt") as f:
	str1 = f.read()

str2 = str1.replace("utilize", "use")

with open("samp2.txt", "w") as f2:
	f2.write(str2)
