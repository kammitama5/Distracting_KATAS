def accum(s):
      arr = []
      
      a = list(s)
      for i in range(0, len(a)):
        b = a[i].upper() + (a[i] * i).lower()
        arr.append(b)
      b = ("-").join(arr)
      return b
	  
	  