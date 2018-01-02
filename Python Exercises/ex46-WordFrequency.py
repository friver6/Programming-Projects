#Counts the frequency of words in a file.

with open("ejemploText.txt") as f:
	fileWords = f.read().split()

#Creates a list of sublists with the ocurrences of each term.
l1 = [[x, fileWords.count(x)] for x in set(fileWords)]

#Sorts list in descending order.
l1.sort(key=lambda x: x[1], reverse=True) 

#Produces 'Histogram'
for item in l1:
	print("{:8}: {}".format(item[0], ("*" * (item[1]))))

