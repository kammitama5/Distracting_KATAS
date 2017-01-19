def tail_swap(strings):
      arr = []
      a = strings[0]
      b = strings[1]
      a1 = a.split(":")
      b1 = b.split(":")
      c = a1[0]
      c1 = a1[1]
      d = b1[0]
      d1 = b1[1]
      
      x =  c + ":" + d1
      y =  d + ":" + c1
      
      r = arr.append(x)
      r1 = arr.append(y)
      
      return arr
	  