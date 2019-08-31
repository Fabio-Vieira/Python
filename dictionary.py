name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if not line.startswith("From "): continue
    else: line = line.split()
    sender = line[1]
    dic[sender] = dic.get(sender,0) + 1

bigcount = None
bigword = None
for word, count in dic.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount
