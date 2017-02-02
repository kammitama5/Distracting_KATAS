
import math
def geometric_sequence_sum(a, r, n):
        arr = []
        x = n - 1
        lastelem = int(a * math.pow(r, x))
       #print lastelem
        for i in range(0, n):
          g = (a * math.pow(r, i))
          arr.append((g))
         
        return sum(arr)
		
		
		