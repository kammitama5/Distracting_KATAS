def reverse_it(data):
      
      if ((type(data) == int)):
        a = str(data)
        b = a[::-1]
        return int(b)
      elif ((type(data) == float)):
        a = str(data)
        b = a[::-1]
        return float(b)
          
      elif (type(data) == str):
        return data[::-1]
        
      else:
        return data
		
		