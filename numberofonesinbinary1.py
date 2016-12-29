def ones(n):
  w = bin(n)
  counter = 0
  for i in w:
    if i == "1":
      counter = counter + 1
  return counter

