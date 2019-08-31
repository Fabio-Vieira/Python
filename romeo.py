fname = raw_input("Enter the file: ")
fhand = open(fname)
lst = list()
for line in fhand:
     line = line.rstrip()
     line = line.split()
     for line in line:
         if not line in lst:
             lst.append(line)
     lst.sort()
print lst