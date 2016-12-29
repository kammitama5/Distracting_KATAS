def count_by(x, n):
  g = x
  w = (x * n) + 1
  
  a = []
  for i in xrange(g, w, x):
    a.append(i)
  return a