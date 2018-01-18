# Originally exercise 50 was supposed to use Rotten Tomatoes' API in order to
# provide the user with a movie's ratings, description and recommendation, but
# that API is unavailable at the moment, so I decided to make this little program
# to use NASA's Open API to show which asteroids are near us today.

import requests
import datetime

#Extract the current day.
now = datetime.datetime.now()
sDate = now.strftime("%Y-%m-%d")

#Turn the requested information into json
astData = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key=DEMO_KEY".format(sDate, sDate))
astDict = astData.json()

print("Asteroids currently nearest our planet.\n")

#Parse through the file gathering relevant information.
for ast in astDict['near_earth_objects'][sDate]:
	print("Name: {}".format(ast["name"]))
	print("Minimum estimated diameter: {:0.2f} m".format(ast["estimated_diameter"]["meters"]["estimated_diameter_min"]))
	print("Potentially dangerous: {}".format(ast["is_potentially_hazardous_asteroid"]))
	print("Relative velocity: {:0.2f} km-s".format(float(ast["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])))
	print("Miss distance from Earth: {:0.2f} km\n".format(float(ast["close_approach_data"][0]["miss_distance"]["kilometers"])))
	
	


