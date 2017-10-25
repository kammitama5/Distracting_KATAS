def repeats(arr):
    arr1 = []
    arr2 = []
    total = 0
    for i in arr:
      if arr.count(i) == 2:
        arr1.append(i)
      else:
        arr2.append(i)
    for i in arr2:
      total = total + i
    return total
	