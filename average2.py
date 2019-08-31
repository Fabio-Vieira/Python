fname = raw_input("Enter the file name: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:    0.8475"):
       continue
    data = line.find(" ")
    num = line[data + 2: data + 8]
    num = float(num)
    count = count + 1
    sum = sum + num
print "Average spam confidence:", sum/count