def reverse_factorial(num):
  
  fact = num;
  reverse = 1;
  g = 1
  while (True):
    if (fact / reverse == 1):
      print str(reverse) + '!';
      
    elif (fact / reverse < 1):
      print fact / reverse
      print -1
      break;
    fact = fact / reverse
    reverse = reverse + 1;
  
   
    
   
  return


reverse_factorial(120)
#reverse_factorial(150)