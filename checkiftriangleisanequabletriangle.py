import math
def equable_triangle(a,b,c): 
  try:
      perimeter = a + b + c 
      p = perimeter / 2.0 
      p1 = p - a 
      p2 = p - b 
      p3 = p - c 
      
      area = math.sqrt(p * p1 * p2 * p3)
    
      if (area == perimeter):
          return True
      elif (area < 0) or (perimeter < 0):
          return False
      else:
          return False
  except:
    return False
	
	