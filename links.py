# Note - this code must run in Python 2.x 

import urllib
from bs4 import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: ')) - 1

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

if count > 0:
	print "Retrieving: ", url
	for i in range(count):
		tags = soup('a')
		url = tags[pos].get('href', None)
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")
		print "Retrieving: ", tags[pos].get('href', None)
else:
	print "Please enter a positive number"