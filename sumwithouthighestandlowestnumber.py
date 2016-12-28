def sum_array(arr):
  
  if (arr == None):
    return 0
  
  elif (len(arr) <= 1):
    return 0
  
    
  else:
    w = sorted(arr)
    del w[-1:]
    del w[0]
    counter = 0 
    for i in w:
      counter = counter + i 
    
    
    return counter
  
  
