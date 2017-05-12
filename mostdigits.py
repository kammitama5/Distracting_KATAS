def find_longest(arr):
      arr1 = []
      arr2 = []
      arr3 = []
      
      for i in arr:
        arr1.append(str(i))
        arr2.append(len(str(i)))
      
      g = max(arr2)
      
      for i in arr:
        if len(str(i)) == g:
          arr3.append(i)
        
      
      return arr3[0]
        
    