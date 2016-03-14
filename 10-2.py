name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
tpl = list()
for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[5:6]
    line = line[0].split(':')
    line = line[0].split()
    for i in line:
        d[i] = d.get(i, 0) + 1

for k,v in d.items():
    tpl.append( (k,v) )
    
tpl.sort()
for k,v in tpl:
    print k,v