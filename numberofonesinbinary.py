
def ones(n):
  w =  bin(n)
  x = str(w)
  y = x[2:]
  
  counter = 0
  for i in y:
    if i == "1":
      counter = counter + 1
  return counter