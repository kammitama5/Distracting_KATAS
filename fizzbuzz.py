def fizz_buzz(n):
  
  if (((n % 3) == 0) and ((n % 5) == 0)):
    print "Fizz Buzz"
  elif ((n % 3) == 0):
    print "Fizz"
  elif ((n % 5) == 0):
    print "Buzz"
  else:
    stringone = str(n)
    print(stringone)
    
  
  return









fizz_buzz(3) # return "Fizz"
fizz_buzz(5) # return "Buzz"
fizz_buzz(15) # return "Fizz Buzz"
fizz_buzz(23) # return num as string