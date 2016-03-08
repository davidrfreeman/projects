fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	# this creates a list of each line
    line = line.split()
    # second loop to go over each word in lists
    for i in line:
    	# checks to see if each word is unique
    	# and if so adds it to the originaly empty array
    	if i not in lst:
    		lst.append(i)
lst.sort()
print lst