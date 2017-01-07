def add_length(str_):
  
      print str_
      if len(str_) == 1:
        a = list(str_)
        for i in range(0, 1):
          a.append("1")
        print a
        
      return 
    
    
    
add_length('apple ban') #["apple 5", "ban 3"])
add_length('you will win') #["you 3", "will 4", "win 3"])
add_length('you') #["you 3"])
add_length('y') # ["y 1"])

