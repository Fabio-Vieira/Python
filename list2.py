fname = raw_input("Enter the File: ")
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    line = line.split()
    for line in line:
        if line in lst: continue
        lst.append(line)
lst.sort()
print lst