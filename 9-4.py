count = dict()
bigWord = None
bigCount = None
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1:2]
    for i in line:
        count[i] = count.get(i, 0) + 1
for a,b in count.items():
	if bigWord == None or b > bigCount:
		bigWord = a
		bigCount = b
print bigWord, bigCount