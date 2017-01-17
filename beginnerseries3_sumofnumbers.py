def get_sum(a,b):
    count = 0
    if (a > b):
      for i in range(b, a+ 1):
        count = count + i 
    elif (b > a):
      for i in range(a, b+1):
        count = count + i 
    else:
        count = a
    return count
	
	