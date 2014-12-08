import urllib3
import json

def fetchSubreddit(name): #fetches JSON string from Reddit and returns it as a Python dictionary
	url = "http://www.reddit.com/r/" + name + "/.json" 
	http = urllib3.PoolManager()
	r = http.request('GET',url) #gets JSON from url
	data = json.loads(r.data.decode("ascii"))
	return data

def getLinks(postArray): #returns list of links from subreddit
	linkList = []
	for item in postArray:
		linkList.append(item["data"]["url"])
	return linkList
