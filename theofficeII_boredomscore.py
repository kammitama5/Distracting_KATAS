 
def boredom(staff):
      #a = boredom.keys()
      count = 0
      for k, v in staff.items():
        if v == 'accounts':
          count = count + 1 
        elif v == 'finance':
          count = count + 2 
        elif v == 'canteen':
          count = count + 10 
        elif v == 'regulation':
          count = count + 3 
        elif v == 'trading':
          count = count + 6
        elif v == 'change':
          count = count + 6 
        elif v == 'IS':
          count = count + 8
        elif v == 'retail':
          count = count + 5 
        elif v == 'cleaning':
          count = count + 4 
        elif v == 'pissing about':
          count = count + 25 
        else:
          count = count 

      if count < 80:
        return "kill me now"
      elif (count > 80) and  (count < 100):
        return "i can handle this"
      elif count > 100:
        return "party time!!"
		
		