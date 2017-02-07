import math
def heron(a, b, c):
      s = (a + b + c) / 2 
      a1 = s - a 
      b1 = s - b 
      c1 = s - c
      A = math.sqrt(s * a1 * b1 * c1)
      return int(A)
	  