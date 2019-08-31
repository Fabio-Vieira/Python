def computegrade(s):
    if s >= 0.9: print "A"
    elif s >= 0.8: print "B"
    elif s >= 0.7: print "C"
    elif s >= 0.6: print "D"
    else:
        if s < 0.6: print "F"
    return ""    
grade = raw_input("Enter the grade: ")
try:
    score = float(grade)
except:
    print "Error! Enter a numeric value!", quit()
print computegrade(score)