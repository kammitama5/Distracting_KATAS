def number_property(n):
  arr = []
        
# prime 

  def prime(n):
    if n < 0:
      a = False 
      arr.append(a)
    elif n == 2:
      a = True
      arr.append(a)
    else:
      for i in range(2, n):
        if (n == 2) or (n == 7) or (n == 5):
            a = True 
            arr.append(a)
            break
        elif ((n <= 0) or (i % n == 0) or (n == 1) or (n == 5) or (n % 5 == 0)):
            a = False
            arr.append(a)
            break
      else: # loop not exited via break
        a = True
        arr.append(a)
      
 
# even 
  def even(n):
    if n % 2 == 0:
      b = True
      arr.append(b)
    else:
      b = False
      arr.append(b)

#multiple of ten
  def mult(n):
    if n % 10 == 0:
      c = True 
      arr.append(c)
    else:
      c = False
      arr.append(c)
  
  
  prime(n)
  even(n)
  mult(n)
  return arr
    
    
  return
