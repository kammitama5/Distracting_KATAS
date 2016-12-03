def divisors(integer):
  ## case find all factors
  
  for i in range(0, integer):
    
    count = 1
    arr = []
    if i % count == 0:
      
      arr.append(i)
      count = count + 1
      if count == integer:
        print arr
          
    else:
      count = count + 1
      if count == integer:
        print(str(integer) + " is prime")
      else: 
        print(str(integer) + " is prime")
    
    return
   
  
    
 
#divisors(15) #[3, 5];
#divisors(12) #[2, 3, 4, 6];
divisors(13) # "13 is prime";