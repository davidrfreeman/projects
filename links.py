# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import *

url = raw_input('Enter: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: ')) - 1

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

links = []

# Retrieve all of the anchor tags
tags = soup('a')

print "Retrieving: ", url

while count > 0:
	# exits once it has looped the number of times given to count
	# loop fills list with all links on page
	for tag in tags:
		links.append(tag.get('href', None))
	html = urllib.urlopen(links[pos]).read()
	soup = BeautifulSoup(html, "html.parser")
	print "Retrieving: ", links[pos]
	# clears out list to be filled again by for loop
	del links[:]
	# removes 1 from count so that the loop will eventually end
	count -= 1