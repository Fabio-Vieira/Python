fname = raw_input("Enter the file name: ")
fhand = open(fname)
count = 0
sum = 0
inp = fhand.read()
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
data = fhand.find(" ")
num = fhand[data + 2: data + 8]
count = count + 1
sum = sum + num
average = sum/ count
print average         