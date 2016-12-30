def last_digit(n1, n2):
    #print n1, n2
    
    
    
    # other cases
    elif (n1 == 1):
      print 1 
    elif (n2 == 1):
      print n1
    elif (n1 == 2) and (n2 % 4 == 0):
      print 6
    elif (n1 == 2) and (n2 % 4 == 1):
      print 2
    elif (n1 == 2) and (n2 % 4 == 2):
      print 4
    elif (n1 == 2) and (n2 % 4 == 3):
      print 8
    elif (n1 == 3) and (n2 % 4 == 0):
      print 1
    elif (n1 == 3) and (n2 % 4 == 1):
      print 3
    elif (n1 == 3) and (n2 % 4 == 2):
      print 9 
    elif (n1 == 3) and (n2 % 4 == 3):
      print 7
    elif (n1 == 4) and (n2 % 2 == 0):
      print 6
    elif (n1 == 4) and (n2 % 2 == 1):
      print 4
    elif (n1 == 5):
      print 5
    elif (n1 == 6):
      print 6
    elif (n1 == 7) and (n2 % 4 == 0):
      print 1
    elif (n1 == 7) and (n2 % 4 == 1):
      print 7
    elif (n1 == 7) and (n2 % 4 == 2):
      print 9
    elif (n1 == 7) and (n2 % 4 == 3):
      print 3
    elif (n1 == 8) and (n2 % 4 == 0):
      print 6
    elif (n1 == 8) and (n2 % 4 == 1):
      print 8
    elif (n1 == 8) and (n2 % 4 == 2):
      print 4   
    elif (n1 == 8) and (n2 % 4 == 3):
      print 2
    elif (n1 == 9) and (n2 % 2 == 0):
      print 1
    elif (n1 == 9) and (n2 % 2 == 1):
      print 9
    
    
    
  
    return
	
	
def last_digit(n1, n2):
    #print n1, n2
    
    if (n1 == 0) or (n2 == 0):
      return 0
    elif (n1 == 1):
      return 1 
    elif (n2 == 1):
      return n1
    elif (n1 == 2) and (n2 % 4 == 0):
      return 6
    elif (n1 == 2) and (n2 % 4 == 1):
      return 2
    elif (n1 == 2) and (n2 % 4 == 2):
      return 4
    elif (n1 == 2) and (n2 % 4 == 3):
      return 8
    elif (n1 == 3) and (n2 % 4 == 0):
      return 1
    elif (n1 == 3) and (n2 % 4 == 1):
      return 3
    elif (n1 == 3) and (n2 % 4 == 2):
      return 9 
    elif (n1 == 3) and (n2 % 4 == 3):
      return 7
    elif (n1 == 4) and (n2 % 2 == 0):
      return 6
    elif (n1 == 4) and (n2 % 2 == 1):
      return 4
    elif (n1 == 5):
      return 5
    elif (n1 == 6):
      return 6
    elif (n1 == 7) and (n2 % 4 == 0):
      return 1
    elif (n1 == 7) and (n2 % 4 == 1):
      return 7
    elif (n1 == 7) and (n2 % 4 == 2):
      return 9
    elif (n1 == 7) and (n2 % 4 == 3):
      return 3
    elif (n1 == 8) and (n2 % 4 == 0):
      return 6
    elif (n1 == 8) and (n2 % 4 == 1):
      return 8
    elif (n1 == 8) and (n2 % 4 == 2):
      return 4   
    elif (n1 == 8) and (n2 % 4 == 3):
      return 2
    elif (n1 == 9) and (n2 % 2 == 0):
      return 1
    elif (n1 == 9) and (n2 % 2 == 1):
      return 9
    else:
      return 0
  
  

last_digit(4, 1) # 4)
last_digit(4, 2) # 6)
last_digit(9, 7) # 9)
last_digit(10, 10 ** 10) # 0)
last_digit(2 ** 200, 2 ** 300) # 6)
last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) # 7)

