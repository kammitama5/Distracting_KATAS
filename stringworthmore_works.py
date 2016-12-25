def highest_value(a, b):
      a1 = a.upper()
      b1 =  b.upper()
      #print a1 
      #print b1
      
      counter1 = 0
      counter2 = 0
      
      for i in a1:
         
        counter1 += ord(i) 
      for j in b1:
        
        counter2 += ord(j) 
      if counter1 == counter2:
        return a 
      elif counter1 > counter2: 
        return a 
      elif counter2 > counter1:
        return b 
      else:
        return "None"