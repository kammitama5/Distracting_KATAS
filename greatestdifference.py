def diff(arr):
  arr1 = []
  for i in arr:
    arr1.append(abs(eval(i)))
  if len(arr) == 0:
      return False
  else:
      b = (max(arr1)) 
      
      if b != 0:
        c = arr1.index(b)
        return arr[c]
      else:
        return False
		
		