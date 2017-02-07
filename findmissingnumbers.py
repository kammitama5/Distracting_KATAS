def find_missing_numbers(arr):
    arr1 = []
    if len(arr) <= 1:
      return [] 
    else:
      max1 = max(arr)
      min1 = min(arr)
      for i in range(min1, max1+1):
        arr1.append(i)
      a = set(arr1).symmetric_difference(set(arr))
      ans = sorted(a)
      return ans
      