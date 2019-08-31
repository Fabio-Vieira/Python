def computepay(r, h):
    if h <= 40:
        p = h * r
    else:
        p = 40 * r + ((h - 40) * (1.5 * r))
    return p

hrs = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print 'Enter a numeric value.', quit()
print computepay(rate, hrs)