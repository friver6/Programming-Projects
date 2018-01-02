#Program that converts euros to dollars.

amEuros = float(input("How many euros are you exchanging? "))
exRate = float(input("What is the exchange rate? "))

amount_ex = amEuros * (exRate / 100)

print("{} euros at an exchange rate of {} is {:.2f} U.S. dollars.".format(amEuros, exRate, amount_ex))


