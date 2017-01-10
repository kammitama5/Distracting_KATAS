def grader(score):
        if (type(score) == float) or (type(score) == int) or (int(score) == int):
    
            if ((score >= 0.9) and (score < 1)):
                return "A"
            elif ((score >= 0.8) and (score < 1)):
                return "B"
            elif ((score >= 0.7) and (score < 1)):
                return "C"
            elif ((score >= 0.6) and (score < 1)):
                return "D"
            elif ((score < 0.6) or (score > 1)):
                return "F"
            elif (score == 1):
                return "A"
            else:
                return "F"
        return
		
		