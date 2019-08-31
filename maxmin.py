maxnumber = None
minnumber = None
while True:
    number = raw_input("Enter a number: ")
    if number == "done" : break
    elif maxnumber is None or maxnumber < number:
        maxnumber = number
    else: 
        if minnumber is None or minnumber > number:
            minnumber = number
print maxnumber, minnumber