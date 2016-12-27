def is_prime(num):
  if num == 0:
      print "{} is not prime".format(num)
  if num > 1:
    
    for i in range(2, num):
      if ((num % i) == 0):
        print "{} is not prime".format(num)
        break;
    else:
        print "{} is prime".format(num)
  
 






is_prime(2)
is_prime(30)
is_prime(31)
is_prime(15)
is_prime(0)