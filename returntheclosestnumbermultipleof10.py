def closest_multiple_10(i):
    #print i
    #print i % 10
    
    if (i % 10 == 0):
       print i
    elif (i % 10 >= 1) and (i % 10 < 5):
       r = i - (i % 10)
       print r 
    else:
       r = (10 - (i % 10))
       print r + i
  
    
    
    
    
    
closest_multiple_10(22) # 20
closest_multiple_10(25) # 30
closest_multiple_10(37) # 40
closest_multiple_10(10)
closest_multiple_10(11)
closest_multiple_10(12)
closest_multiple_10(13)
closest_multiple_10(14)

