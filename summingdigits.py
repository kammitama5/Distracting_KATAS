def sumDigits(number):
    sum = 0
    a = str(abs(number))
    b =  list(a) 
    for i in a:
      sum = sum + int(i)
    return sum
    