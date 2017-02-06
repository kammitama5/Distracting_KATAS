def next_id(arr):
      total = 0
      count = 0
      b = sorted(arr)[-1]
      print sorted(arr)
      for i in range(0, b+1):
        count = count + i 
      for i in arr:
        total = total + i
      if len(arr) == 0:
        print 0 
      elif (total != count):
        diff = count - total 
      elif (sorted(arr)[0] != 0):
        print 0
      else:
        print sorted(arr)[-1] + 1
     
        
      
      return