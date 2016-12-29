def count_arara(n):
  if (n == 1):
    return "anane"
  elif (n == 2):
    return "adak"
  elif (n % 2) == 0:
     
    return ("adak " * (n / 2)).rstrip()
  else:
      q = ("adak " * ((n - 1) / 2) + "anane")
      return q.rstrip()
    
    
