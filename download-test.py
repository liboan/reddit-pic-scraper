import urllib3
import json

http = urllib3.PoolManager()
r = http.request('GET',"http://www.reddit.com/r/EarthPorn/.json") #gets JSON from url
print(r.status)

print(type(r.data))
data = r.data.decode("ascii")

data = json.loads(data)
print(type(data))
#print(data["data"]["children"][0]["kind"]) #going to have to do some crazy dict stuff

for item in data["data"]["children"]:
	print("%d \t %s \t %s" % (item["data"]["score"], item["data"]["domain"],  item["data"]["url"]))