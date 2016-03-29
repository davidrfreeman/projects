import xml.etree.ElementTree as ET
import urllib

url = raw_input("Enter HTML: ")

XML_response = urllib.urlopen(url).read()

tree = ET.fromstring(XML_response)

nums = tree.findall('.//count')

total = 0

for i in nums:
	total = total + int(i.text)

print total




