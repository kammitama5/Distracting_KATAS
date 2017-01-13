def process_data(data):
      prod = 1
      
      for i in data:
        a = i[0] - i[1]
        prod = prod * a
      return prod
	  
	  