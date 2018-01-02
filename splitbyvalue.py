def split_by_value(k, elements):
    
    arr = []
    arr1 = []
    
    for i in elements:
      if i < k:
        arr.append(i)
      else:
        arr1.append(i)
    return arr+arr1
	