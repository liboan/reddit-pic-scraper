import urllib3
import json
from datetime import datetime
import re

def checkURL(url): #checks URL if it's a picture
	isPicture = re.compile(r".(jpg|png|gif)")
	if isPicture.search(url):
		return True
	else:
		return False

	# if re.compile(r".(jpg)").search(url):
	# 	return "jpg"
	# elif re.compile(r".(png)").search(url):
	# 	return "png"
	# elif re.compile(r".(gif)").search(url):
	# 	return "gif"
	# else:
	# 	return False

def fetchImage(url, name): #Fetches image from url and names it according to parameter name
	http = urllib3.PoolManager()
	request = http.request("GET", url)
	if request.status == 200:
		image = request.data
		file = open(name+".jpg", 'wb')
		file.write(image)
		file.close()
		return True
	else: 
		return False