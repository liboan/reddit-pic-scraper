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

def fetchImage(url, name, infoArray): #Fetches image from url and names it according to parameter name
	http = urllib3.PoolManager()
	request = http.request("GET", url)
	if request.status == 200:
		image = request.data
		file = open(name+".jpg", 'wb')
		file.write(image)
		file.close()
		addToJSON(url, name, infoArray)
		return True
	else: 
		return False

def openJSONLog():
	jsonLog = open("log.json", "r+").read() #pull string out of the file
	if len(jsonLog) == 0: #if not created yet, return empty list
		return []
	else: #otherwise, return the list from the json file
		return json.loads(jsonLog) 

def addToJSON(url, name, infoArray): #accepts infoArray and adds an object with url, name, and time to it
	logObj = {"url": url, "name": name, "date": str(datetime.now())}
	infoArray.append(logObj)
	# jsonLog = open("log.json", 'a+')
	# json.dump(logObj, jsonLog)
	# jsonLog.close()

def writeJSONLog(infoArray):
	jsonLog = open("log.json", 'w+')
	json.dump(infoArray, jsonLog)
	jsonLog.close()
