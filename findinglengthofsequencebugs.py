def length_of_sequence(arr,n):
      arr2 = []
      if len(arr) == 2:
        return 2 
      else:
        for i, j in enumerate(arr):
          if (i == n) or (j == n):
            arr2.append(i)
          
        a = arr2[0]
        b =  arr2[1]
        return (b - a) + 1
        