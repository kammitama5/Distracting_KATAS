import math
def pythagorean_triple(integers):
    a = integers[0]
    b = integers[1]
    c = integers[2]
    
    a1 = math.pow(a, 2)
    b1 = math.pow(b, 2)
    c1 = math.pow(c, 2)
    
    if ((c > a) and (c > b) and (a > 0) and (b > 0) and (c > 0)) and (a1 + b1 == c1):
      return True
    else:
      return False
      
    return

pythagorean_triple([3, 4, 5])#, True)
pythagorean_triple([3, 5, 9])#, False)
