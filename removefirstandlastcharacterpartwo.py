def array(string):
    if (len(string) <= 4):
      return None 
    else:
      a1 = string.replace(" ", "")
    
      b = a1.split(",")
      b1 = (" ").join(b)
      return b1[2:-2]
	  
	  