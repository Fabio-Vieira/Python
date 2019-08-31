fname = raw_input("Enter the file: ")
fhand = open(fname)
counts = dict()
for line in fhand:
    if not line.startswith("From "): continue
    else: line = line.split()
    sender = line[1]
    counts[sender] = counts.get(sender, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print bigcount, bigword


