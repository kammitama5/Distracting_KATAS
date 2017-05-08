def calculate(string):
      b = [int(s) for s in string.split() if s.isdigit()]
      c = string.split(' ')
      
      if 'gains' in c:
        diff = b[0] + b[1]
      elif 'loses' in c:
        diff = b[0] - b[1]
      return diff
	  