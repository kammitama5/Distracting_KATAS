def average(x):
  sum = 0
  
  for j in x:
    if type(j) is str:
      return("Incorrect")
    else:
      sum += j
  for i in x:
    if type(i) is str:
      return("Incorrect")
    else:
      for i in x:
        avg = (sum / len(x))
  return avg