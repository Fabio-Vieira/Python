fname = raw_input("Enter the file: ")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("From "): continue
    else: line = line.split()
    count = count + 1
    print line[1]
print count

    
