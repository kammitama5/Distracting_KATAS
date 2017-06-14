# return a sorted set with the difference
def diff(a, b):
  a1 = set(a)
  b1 = set(b)
  c = list(a1 - b1)
  c1 = list(b1 - a1)
  d = c + c1
  return sorted(d)
  