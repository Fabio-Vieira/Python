#Shows the ten most common words in a file
fname = raw_input('Enter File: ')
fhand = open(fname)
counts = dict()
for line in fhand:
    word = line.split()
    for word in word:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    lst.append( (v, k) )
lst.sort(reverse=True)
for v, k in lst[:10]:
    print v, k