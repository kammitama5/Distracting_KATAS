def solve(s):
  arr = []
  import itertools
  a = (s[i:j] for i, j in itertools.combinations(xrange(len(s)+1), 2))
  for i in a:
    if int(i) % 2 != 0:
      arr.append(i)
  return len(arr)
  