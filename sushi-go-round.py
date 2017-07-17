def total_bill(s):
    if len(s) == 0:
      print 0
    else:
      arr = []
      a1 = list(s)
      
      a1 = [x.strip(' ') for x in a1]
      a2 = ''.join(a1)
      #print a2
     
      a = len(a2) / 5
      #print a
      b = len(a2) *  2
      #print b
      c = b - a - a 
      return c
	  
	  