import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    lst = re.findall("^X\S*: ([0-9.]+)", line)
    if len(lst) > 0:
        print lst