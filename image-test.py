import urllib3
import json
from datetime import datetime
import re

http = urllib3.PoolManager()
imgURL = "http://i.imgur.com/1qzb8tn.jpg?1"
# r = http.request("GET", imgURL)
# image = r.data

def checkURL(url):
	isPicture = re.compile(r".(jpg|png|gif)")
	if isPicture.search(url):
		return True
	else:
		return False

def fetchImage(url, name):
	request = http.request("GET", url)
	image = request.data
	file = open(name+".jpg", 'wb')
	file.write(image)
	file.close()
	

# file = open("test.jpg",'wb')
# file.write(image)
# file.close()

if checkURL(imgURL):
	fetchImage(imgURL,"picture")
	logObj = {"url": imgURL, "name": "test", "timeFetched": str(datetime.now())}
	print(datetime.now().replace(microsecond=0))
	print(json.dumps(logObj))
	jsonLog = open("log.json","w")
	json.dump(logObj,jsonLog)
	jsonLog.close()

else:
	print("NOT AN IMAGE")

