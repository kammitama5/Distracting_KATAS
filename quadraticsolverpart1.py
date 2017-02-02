import math
def solver(a, b, c):
    arr = []
    x1 = (math.sqrt((b * b) - (4 * a * c)))
    x2 = -1 * b 
    x3 = 2 * a 
    x = (x2 + x1) / x3 
    y = (x2 - x1) / x3
    
    first = round(x, 2)
    second = round(y, 2)
    
    if (first == second):
      arr.append(first)
    else:
      arr.append(first)
      arr.append(second)
    return arr 
	