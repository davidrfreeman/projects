import json
import urllib

address = raw_input("Enter Location: ")

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})

data = urllib.urlopen(url).read()

js = json.loads(str(data))

# print json.dumps(js, indent=4)

placeid = js["results"][0]["place_id"]

print "Place ID: ", placeid

