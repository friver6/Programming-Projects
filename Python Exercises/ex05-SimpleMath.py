#Prompts for two numbers, and then prints a series of operations with them.

fnumber = input("What is the first number? ")
snumber = input("What is the second number? ")

print("{} + {} = {}". format(fnumber, snumber, int(fnumber) + int(snumber)))
print("{} - {} = {}". format(fnumber, snumber, int(fnumber) - int(snumber)))
print("{} * {} = {}". format(fnumber, snumber, int(fnumber) * int(snumber)))
print("{} / {} = {}". format(fnumber, snumber, int(fnumber) / int(snumber)))
