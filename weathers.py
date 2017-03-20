import sys,json
if len(sys.argv) !=2:
	raise SystemExit('Usage:*.py id')
cityid=sys.argv[1]

import urllib.request,codecs
url="https://works.ioa.tw/weather/api/weathers/{}.json".format(cityid)
response = urllib.request.urlopen(url).read().decode('utf8')
obj=json.loads(response)
print (obj)
