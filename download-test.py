import urllib3
import json

http = urllib3.PoolManager()
r = http.request('GET',"http://www.reddit.com/r/civ/.json") #gets JSON from url
print(r.status)

print(type(r.data))
data = r.data.decode("ascii")

data = json.loads(data)
print(type(data))
print(data["data"]["children"][0]["kind"]) #going to have to do some crazy dict stuff