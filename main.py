import urllib3
import json
from datetime import datetime
import re
import os.path

urllib3.disable_warnings() #disable warning from popping up on console- perhaps implement HTTPS as they suggest?

#import image-related functions for project
import image

#import Reddit JSON-related functions for project
import reddit

def timeString(): #creates timestring for file names
	string = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + "_" + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
	return string

subreddit = input("Enter a subreddit\n")

directory = "images/" #directory in which images will be stored

print("Fetching data from /r/" + subreddit)

data = reddit.fetchSubreddit(subreddit)
linkArray = reddit.getLinks(data["data"]["children"])

initTime = timeString() #get initial time for file names

imgCount = 0

urlArray = [] #list of urls from reddit that are images

imageInfoArray = [] #list of image info objects from this session

arrayFromJSON = [] #list pulled from JSON log

if os.path.isfile("log.json"):
	print("opening log.json")
	arrayFromJSON = image.openJSONLog()
else: 
	print("creating log.json")
	file = open("log.json", "w+")

for url in linkArray: #placeholder for now- pulls only the image links from the subreddit link list, to be counted
	if (image.checkURL(url) != False):
		imgCount = imgCount + 1
		urlArray.append(url) 

print("Starting download of " + str(len(urlArray)) + " images from /r/" + subreddit)

for num, url in enumerate(urlArray,start=1): #iterates through imageInfoArray, names files with initTime + index, then downloads.
	name = directory + initTime + "_" + str(num)
	print("Downloading image " + str(num) + " of " + str(1+len(imageInfoArray)))
	image.fetchImage(url,name, imageInfoArray)

print(imageInfoArray)
image.writeJSONLog(arrayFromJSON + imageInfoArray) #merge two arrays and write


