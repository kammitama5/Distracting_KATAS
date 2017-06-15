def case_unification(n):
    l = 0
    u = 0
    
    for i in n:
      if i == i.lower():
        l = l + 1 
      elif i == i.upper():
        u = u + 1 
        
    if l > u:
      return n.lower()
    else:
      return n.upper()
	  