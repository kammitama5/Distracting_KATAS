import collections
def solve(s):
  arr = []
  a = list(s)
  for i in range(1, len(a)):
    b = collections.deque(a)
    b.rotate(i)
    c = ''.join(list(b))
    if c == c[::-1]:
      arr.append(c)
  if len(arr) > 0:
    return True
  else:
    return False
	