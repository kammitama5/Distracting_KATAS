def next_perfect_square(n):
    import math
    if n == 0:
      return 1 
    elif n < 0:
      return 0
    else:
      a = int(math.sqrt(n)) + 1
      b = pow(a, 2)
      return b
	  
	  