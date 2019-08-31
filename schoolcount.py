fname = raw_input("Enter the file: ")
if len(fname) < 1: fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    if not line.startswith("From "): continue
    else: line = line.split()
    sender = line[1].split('@')
    counts[sender[1]] = counts.get(sender[1], 0) + 1
print counts    
     