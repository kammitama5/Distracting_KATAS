def elimination(arr):
  try:
        arr1 = []
        
        for i in arr:
         if arr.count(i) == 2:
           arr1.append(i)
       
        return arr1[0]
        
  except:
    return None
	