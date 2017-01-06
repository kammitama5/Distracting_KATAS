def sumDigits(number):
      a = abs(number)
      a1 = str(a)
      
      sum1 = sum(int(x) for x in a1 if a1.isdigit())
      return sum1
	  
	  