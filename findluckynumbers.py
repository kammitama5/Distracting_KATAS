def filter_lucky(lst):
  arr = []
  for i in lst:
    g = str(i)
    if "7" in g:
      arr.append(int(g))
  return arr
  
  
