import urllib3
import json
from datetime import datetime
import re

urllib3.disable_warnings() #disable warning from popping up on console- perhaps implement HTTPS as they suggest?

#import image-related functions for project
import image

#import Reddit JSON-related functions for project
import reddit

def timeString(): #creates timestring for file names
	string = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + "_" + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
	return string

subreddit = "spaceporn"

directory = "images/" #directory in which images will be stored

print("Fetching data from /r/" + subreddit)

data = reddit.fetchSubreddit(subreddit)
linkArray = reddit.getLinks(data["data"]["children"])

initTime = timeString() #get initial time for file names

imgCount = 0
imageLinkArray = []

for url in linkArray: #placeholder for now- pulls only the image links from the subreddit link list, to be counted
	if (image.checkURL(url) != False):
		imgCount = imgCount + 1
		imageLinkArray.append(url) 

print("Starting download of " + str(len(imageLinkArray)) + " images from /r/" + subreddit)

for num, url in enumerate(imageLinkArray,start=1): #iterates through imageLinkArray, names files with initTime + index, then downloads.
	name = directory + initTime + "_" + str(num)
	print("Downloading image " + str(num) + " of " + str(len(imageLinkArray)))
	image.fetchImage(url,name)


