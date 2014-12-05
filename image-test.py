import urllib3
import json

http = urllib3.PoolManager()
imgURL = "http://i.imgur.com/XDvF40M.jpg"
r = http.request("GET", imgURL)
image = r.data

file = open("test.jpg",'wb')
file.write(image)
file.close()

logObj = {"url": imgURL, "name": "test"}

print(json.dumps(logObj))

jsonLog = open("log.json","w")
json.dump(logObj,jsonLog)
jsonLog.close()
