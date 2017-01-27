def first_dup(s):
    arr = []
    for i in s:
      if s.count(i) > 1:
        a = i 
        arr.append(a)
    
    if arr == []:
      return None 
    else:
      return arr[0]
     