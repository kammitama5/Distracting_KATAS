def fizzbuzz(n):    
    arr = []
    for n in range(1, n+1):
      if ((n % 5 == 0) and (n % 3 == 0)):
          a = arr.append("FizzBuzz")
        
      elif (n % 5 == 0):
          a = arr.append("Buzz")
      elif (n % 3 == 0):
          a = arr.append("Fizz")
      else:
          a = arr.append(n)
        
    return arr
	
	