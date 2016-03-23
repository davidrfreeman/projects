import json
import urllib

url = raw_input("Enter URL: ")

data = urllib.urlopen(url).read()

parsed = json.loads(data)

total = 0

for i in parsed['comments']:
	total = total + int(i['count'])

print total