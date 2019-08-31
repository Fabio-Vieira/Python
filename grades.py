grade = raw_input('Enter the grade: ')
try:
    grade = float(grade)
except:
    if grade > 1.0 or grade < 0.0: quit()
if grade >= 0.9: print 'A'
elif grade >= 0.8: print 'B'
elif grade >= 0.7: print 'C'
elif grade >= 0.6: print 'D'
else:
    if grade < 0.6: print 'F'