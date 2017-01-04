import math
def circleArea(r):
    if (type(r) == str):
      return False
    elif r <= 0:
      return False 
    elif (type(r) == float) or (type(r) == int):
      area = math.pi  * (r * r)
      return round(area, 2)
    else: 
      area = math.pi  * (r * r)
      return round(area, 2)
    return
  