def is_lucky(ticket):
  try:
      count = 0 
      count1 = 0
      if len(ticket) < 6:
        return False
      else:
        x = ticket[:3]
        y = ticket[-3:]
        for i in x:
          count = count + int(i)
        for j in y:
          count1 = count1 + int(j)
        if count == count1:
          return True
        else:
          return False
  except:
      return False
	  