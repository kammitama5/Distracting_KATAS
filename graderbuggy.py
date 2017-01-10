def grader(score):
        if (type(score) == float) or (type(score) == int): 
    
            if ((score >= 0.9) and (score < 1)):
                print "A"
            elif ((score >= 0.8) and (score < 1)):
                print "B"
            elif ((score >= 0.7) and (score < 1)):
                print "C"
            elif ((score >= 0.6) and (score < 1)):
                print "D"
            elif ((score < 0.6) or (score > 1)):
                print "F"
            else:
                print "F"
        return
                
                
          


grader(0.9) # == "A"

grader(0.3) #== "F"

grader(234) # == "F"

grader(0.75) #== "C"


grader(0.7) # == "C")
grader(0.9) # == "A")
grader(0.6) # == "D")


