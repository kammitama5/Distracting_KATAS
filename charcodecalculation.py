def calc(x):
  a = list(x)
  one = ""
  for i in a:
    b = ord(i)
    one = one + str(b)
  two = one.replace("7","1")
  
  diff = str(int(one) - int(two))
  count = 0 
  for i in diff:
    count = count + int(i)
  return count
  