#Compares two strings and determines if they are anagrams.

def isAnagram(word1, word2):
	if sorted(word1) == sorted(word2):
		print("'{}' and '{}' are anagrams.".format(word1, word2))
	else:
		print("They are not anagrams.")


print("Enter two strings and I'll tell you if they are anagrams: ")
fString = input("Enter the first string: ")
sString = input("Enter the second string: ")

isAnagram(fString, sString)
