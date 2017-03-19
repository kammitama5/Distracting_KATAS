def calculate(string):
      a = string.split(" ")
      b = [int(i) for i in string.split() if i.isdigit()]
      x = b[0]
      y = b[1]
      
      for i in a:
        if i == 'gains':
          result = x + y 
        elif i == 'loses':
          result = x - y
      return result
	  
	  