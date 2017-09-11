def summationOfPrimes(primes):
  total = 0
  for num in range(1,primes + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           total = total + num
  return total
       