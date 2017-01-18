def duplicate_elements(m, n):
  
      a = set(m).intersection(n)
      if len(a) > 0:
        return True
      else:
        return False
		
		