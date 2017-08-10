def closest(l):
    arr = [0]
    arr1 = []
    for i in l:
      arr.append(i)
    g = sorted(arr)
    
    #print g 
    h = (g.index(0))
    #print h
    
    if h == 0:
      arr1.append(g[1])
      #print arr1
    else:
      arr1.append(g[h-1])
      arr1.append(g[h+1])
    #print arr1
    
    if len(arr1) == 1:
      return arr1[0]
    else:
      b = arr1[0]
      c = arr1[1]
      if abs(b) - abs(c) == 0:
        return None 
      elif abs(c) > abs(b):
        return (b)
      else:
        return (c)
      