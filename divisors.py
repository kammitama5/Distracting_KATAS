def divisors(integer):
  ## case find all factors
  if (integer % 2 == 0):
    print "Hi"
  ## case prime
  else:
    print(str(integer) + " is prime")
  
  return

#divisors(15) #[3, 5];
#divisors(12) #[2, 3, 4, 6];
divisors(13) # "13 is prime";

