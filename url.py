import urllib
from bs4 import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

nums = []

tags = soup('span')
for tag in tags:
   nums.append(int(tag.contents[0]))

print sum(nums)