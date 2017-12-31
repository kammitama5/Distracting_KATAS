def pairs(ar):
  
  arr = zip(ar[0::2], ar[1::2])
  count = 0
  for i in arr:
    if abs(i[0] - i[1]) == 1:
      count = count + 1
  return count