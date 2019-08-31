fname = raw_input("Enter the File: ")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("From:"): continue
    else: line = line.split()
    print line[1]
    count = count + 1
print "There were", count, "lines in the file with From as the first word"