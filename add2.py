import urllib.request, json
url="https://works.ioa.tw/weather/api/cates/1.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print (data)
