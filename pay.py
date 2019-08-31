hrs = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
try: 
    hrs = float(hrs)
    rate = float(rate)
except:
    print "Error! Enter a numeric value.", quit()
if hrs <= 40:
    payment = hrs * rate 
else:
    payment = 40 * rate + ((hrs - 40) * (1.5 * rate))
print 'The pay is: ', payment