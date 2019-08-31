hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    hrs = -1
if hrs < 0: print "Error, please enter a numeric value.", quit()
if hrs > 40:
    x = hrs - 40
    x = float(x)
    payment = (40 * rate) + (x * 15)
else:
    payment = hrs * rate
print "Your payment is: ", payment