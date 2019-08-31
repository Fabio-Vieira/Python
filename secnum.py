print "Please, think of a number between 0 and 100!"
x = 100
low = 0
high = x
ans = 0

while abs(ans - x) > 0:
    ans = (high + low) / 2
    print "Is your secret number " + str(ans) + "?"
    userInp = raw_input("Enter l to indicate that your secret number is smaller, enter h to indicate that your secret number is bigger, and enter c to indicate that the guess is correct: ")

    if userInp == 'h':
        low = ans
        continue
    elif userInp == 'l': 
        high = ans
        continue
    elif userInp == 'c':
        print "Game over! Your secret number is " + str(ans)
        break
    else: 
        print "Sorry! I didn't understand your input."