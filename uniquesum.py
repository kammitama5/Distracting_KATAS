def unique_sum(n):
    if len(n) == 0:
        return None
    else:
    
        bum = list(set(n))
        counter = 0
        for i in bum:
          counter = counter + i
      
        return counter
		
		