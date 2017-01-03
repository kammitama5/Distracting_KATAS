import math
def index(array, n):
    x = len(array)
    if n > x:
      return -1
    else:
      a = (math.pow(array[n], n))
      b = int(a)
      return b 
	  
	  