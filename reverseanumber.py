def reverseNumber(n):
      a = str(abs(n))
      b = a[::-1]
      c = int(b)
      if n < 0:
        return 0 - c 
      else:
        return c 
		
		