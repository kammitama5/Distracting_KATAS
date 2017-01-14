
def divisible_by(numbers, divisor):
      arr = []
      for i in numbers:
        if (i % divisor == 0):
          arr.append(i)
          
      return arr
	  
	  