import re
fh = raw_input('Enter file name: ')
name = fh
if len(fh) < 1:
	name = 'regex-sample.txt'
handle = open(name)
nums = list()
for line in handle:
	strList = re.findall('[0-9]+', line)
	if len(strList) == 0: continue
	for i in range(len(strList)):
		number = int(strList[i])
		nums.append(number)

print sum(nums)


