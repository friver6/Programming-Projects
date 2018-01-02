#Prompts for a city name and returns the current temperature for that city (using OpenWeatherMap API).

import requests

usrCity = input("Where are you? ")

#This API requires authentication, so the address contains the pin from a previously created account.
cityW = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid=961d12dd5614492acbde55bcb36c63b7".format(usrCity))

reqInfo = cityW.json()

cityTemp = (reqInfo["main"]["temp"]) * (9/5) - 459.67

print("{} weather: \n{:.2f} degrees Fahrenheit".format(usrCity, cityTemp))




