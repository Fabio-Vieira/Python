count = 0
total = 0
while True:
    number = raw_input("Enter a number: ")
    try:
        number = float(number)
    except:
        print "Invalid Input."
    if number == "done": break
    else:
        total = total + number
        count = count + 1
        average = total/count
print count, total, average