def count_sheeps(arrayOfSheeps):
  count = 0
  for i in arrayOfSheeps:
    if i == True:
      count = count + 1
    else:
      count = count
  return count
  