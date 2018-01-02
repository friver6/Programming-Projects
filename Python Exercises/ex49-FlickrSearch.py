#Takes in a search string and displays photos taken from Flickr that match that string.
import flickrapi
import json

usrTag = input("What do you want to search? ")

api_key = u'b92f689d0b1da0cc6e2bc8b024fc06c4'
api_secret = u'761ce41b9f5d142e'

#Uses flickrapi module to log into the Flickr API authentication site, and extract the information in json format.
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
photos = flickr.photos.search(tags=usrTag)

#Will be turning information from byte, to dict, then finally to a list of dictionaries. I do this to reach deeper into that nested data structure.
photos = photos.decode()
jsonPhotos = json.loads(photos)
psDict = jsonPhotos['photos']['photo']

#Constructs the html file, according to the format given by the Flickr documentation.
with open("siteOutput.html", "w") as f:
	f.write("<!DOCTYPE html>\n\t<html>\n\t\t<head>\n\t\t\t<title>Flickr Request Program</title>\n\t\t</head>\n")
	f.write('\t\t<body>\n\t\t\t<p>Photos about "{}"</p>\n'.format(usrTag))
	for subDict in psDict:
		f.write('\t\t\t<img src="https://farm{}.staticflickr.com/{}/{}_{}.jpg" height="200" width="200">\n'.format(subDict['farm'], subDict['server'], subDict['id'], subDict['secret']))

	f.write("\t\t</body>\n\t</html>")


