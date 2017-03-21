import urllib.request
u=urllib.request.urlopen('http://10.77.14.15:8080/bms/wmserver/list')
data=u.read()
from xml.etree.ElementTree import XML
doc=XML(data)

#for pt in doc.findall('.//serviceIp'):
#print(pt.text)
print (doc)