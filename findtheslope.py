def find_slope(points):
    x1 = points[0]
    x2 = points[2]
    y1 = points[1]
    y2 = points[3]
    
    if ((x2 - x1) == 0):
      return "undefined"
    elif ((y2 - y1) == 0) and ((x2 - x1) == 0):
      return "undefined"
    elif ((y2 - y1) == 0) or ((x2 - x1) == 0):
      return "0"
    elif (((y2 - y1) / (x2 - x1)) == 0):
      return "undefined"
    else:
      return str((y2 - y1) / (x2 - x1))
	  
	  