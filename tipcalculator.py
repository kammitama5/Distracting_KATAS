import math
def calculate_tip(amount, rating):
      #rating1 = re.match('[a-z]+$', rating)
      rating1 = rating.lower()
      terrible = 0
      poor = .05 
      good = .10 
      great = .15 
      excellent = .20
      
      if (rating1 == "terrible"):
        tip = amount * terrible 
        tip1 = (math.ceil(tip))
        tip2 = round(tip1, 0)
        return tip2
      elif (rating1 == "poor"):
        tip = amount * poor
        tip1 = (math.ceil(tip))
        tip2 = round(tip1, 0)
        return tip2
      elif (rating1 == "good"):
        tip = amount * good
        tip1 = (math.ceil(tip))
        tip2 = round(tip1, 0)
        return tip2
      elif (rating1 == "great"):
        tip = amount * great
        tip1 = (math.ceil(tip))
        tip2 = round(tip1, 0)
        return tip2
      elif (rating1 == "excellent"):
        tip = amount * excellent
        tip1 = (math.ceil(tip))
        tip2 = round(tip1, 0)
        return tip2
      else:
        return "Rating not recognized"
		
		
        