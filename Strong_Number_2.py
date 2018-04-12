def factorial (n):
    fact = 1 
    for i in range(1, n+1):
      fact = fact * i 
    return fact


def strong_num(number):
    arr = []
    fact = 1 
    sum1 = 0 
    num = list(str(number))
    #print num
    
    for i in num:
      arr.append(factorial(int(i)))
    
    for i in arr:
      sum1 = sum1 + i 
    if sum1 == number:
      return "STRONG!!!!"
    else:
      return 'Not Strong !!'