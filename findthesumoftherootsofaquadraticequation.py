import math
def roots(a,b,c):
    try:
      arr = []
      x1 = (math.sqrt((b * b) - (4 * a * c)))
      x2 = -1 * b 
      x3 = 2 * a 
      x = (x2 + x1) / x3 
      y = (x2 - x1) / x3
      
      first = round(x, 2)
      second = round(y, 2)
      
      sum1 =  (first + second) 
      return round(sum1, 2)
    except:
      return None
	  