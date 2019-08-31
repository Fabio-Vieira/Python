fname = raw_input("Enter the file: ")
fhand = open(fname)
dic = dict()
for line in fhand:
    if not line.startswith("From "): continue
    else: line = line.split()
    sender = line[5].split(':')
    for line in sender[:1]:
        dic[line] = dic.get(line, 0) + 1
    
lst = list()
for k, v in dic.items():
    lst.append((k, v))
lst.sort()
for k, v in lst:
    print k, v
    