import urllib3

http = urllib3.PoolManager()
r = http.request('GET',"http://www.reddit.com/r/WorldofTanks/.json")
print(r.status)
print(r.data)