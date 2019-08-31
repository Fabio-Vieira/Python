largest = None
smallest = None
while True:
    num = raw_input("Enter a numeric value: ")
    try :
        num = int(num)
    except:
        print "Invalid Input"
    if num == "done": 
        break
    elif largest is None or num > largest:
        largest = num
        continue
    elif smallest is None or num < smallest:
        smallest = num
print "Maximum", largest
print "Minimum", smallest 
