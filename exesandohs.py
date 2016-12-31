def xo(s):
    h = s.lower()
    
    
    countx = 0 
    county = 0 
    
    for i in h:
      if i == 'x':
        countx = countx + 1
      elif i == 'o':
        county = county + 1
      else:
        "I don't care"
    
    if countx == county:
      return True
    else:
      return False
	  
	  