def two_highest(list1):
    if type(list1) == str:
      return False
    else:
      a = set(list1)
      b = list(a)
      c = sorted(b)
      d = c[::-1]
      return d[:2]
  