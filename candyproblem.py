def candies(s):
    arr = []
    
    if ((len(s) <= 1) or (s == [])):
      return -1
    else:
      a = max(s)
      for i in s:
        diff = a - i 
        arr.append(diff)
      return sum(arr)
	  