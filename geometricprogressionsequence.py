import math
def geometric_sequence_elements(a, r, n):
        arr = []
        x = n - 1
        
        lastelem = int(a * math.pow(r, x))
        #print lastelem
        
        for i in range(0, n):
          g = int(a * math.pow(r, i))
          arr.append(str(g))

        c = (', ').join(arr)
        return c
		
		