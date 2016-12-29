def summation(x):
  if type(x) !=  int:
    return "Error 404"
  else:
    counter = 0
    for i in range(0, (x + 1)):
      counter = counter + i
    return counter
	
	