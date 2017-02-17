def numbers_with_digit_inside(x, d):
    count = 0 
    sum1 = 0
    product = 1
    
    arr = []
    # loop through all values in range from 1 to number (incl)
    # if there is instance of digit -> 
    # add count -> count + 1 
    # add sum -> sum + i 
    # set product to 1 and * product -> product = product * i 
    if x < d or x == d:
      arr = [0, 0, 0, 0, 0]
    else:
      for i in range(1, x+1):
        #print str(i)
        if str(d) in str(i):
          a = int(i)
          count = count + 1 
          sum1 = sum1 + a 
          product = product * a  
           
          arr.append(count)
          arr.append(sum1)
          arr.append(product)
        elif x < d:
          arr.append[0,0,0]
          
    print arr[-3:]
      
    
    
    
    return
  