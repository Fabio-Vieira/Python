fname = raw_input("Enter a file: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    else:
       data = line.find("0")
       number = line[data: data + 6]
       number = float(number)
       count = count + 1
       total = total + number
average = total / count
print "The Average Spam Confidence is:", average