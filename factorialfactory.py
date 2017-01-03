def factorial(n):
    if (n < 0):
      return None
    elif (n == 0):
      return 1 
    else:
      counter = 1 
      for i in range(1, n+ 1):
        counter = counter * i
    return counter
	
	