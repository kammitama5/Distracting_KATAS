def calculate_grade(scores):
      counter = 0
      len1 = len(scores)
      for i in range(0, len1):
        counter = counter + scores[i]
      mean = int(counter / len1)
      
      if (mean < 60):
        return "F"
      elif (mean < 70):
        return "D"
      elif (mean < 80):
        return "C" 
      elif (mean < 90):
        return "B" 
      else:
        return "A"
		
		