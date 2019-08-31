fname = raw_input("Enter file name: ")
fhand = open(fname)
fhand = fhand.read()
lst = list()
for line in fhand:
    line = line.rstrip().split()
    for line in line:
        if line in lst: continue
        lst.append(line)
lst.sort()
print lst