
def mxdiflg(s1, s2):
    arr = []
    arr1 = []
    if (len(s1) == 0) or (len(s2) == 0):
      return -1 
    else:
      for i in s1:
        arr.append(len(i))
      for j in s2:
        arr1.append((len(j)))
      a = max(arr)
      a1 = min(arr)
      b = max(arr1)
      b1 = min(arr1)
      
      c = max(a, a1, b, b1)
      d = min(a, a1, b, b1)
      ans = c - d
      return ans
    
    return
    
   
  