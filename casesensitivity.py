def case_sensitive(s):
  arr = []
  arr1 = []
  a = list(s)
  for i in a:
    if i == i.upper():
      arr.append(i)
  if len(arr) > 0:
    arr1.insert(0, arr)
    arr1.insert(0, False)
  else:
    arr1 = [True, []]
  return arr1
  