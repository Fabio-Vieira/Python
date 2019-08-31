epsilon = 0.01
y = float(raw_input("Enter a number: "))
guess = y / 2

while abs(guess * guess - y) >= epsilon:
    guess = guess - (((guess ** 2) - y)/(2 * guess))
print ('Square root of ' + str(y) + ' is about ' + str(guess))
