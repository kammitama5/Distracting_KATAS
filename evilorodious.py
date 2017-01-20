def evil(n):
    count = 0
    a =  list(bin(n))
    for i in a:
      if i == '1':
        count = count + 1 

    if (count % 2 == 0):
      return "It's Evil!"
    else:
      return "It's Odious!"
	  
	  