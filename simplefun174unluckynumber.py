def unlucky_number(n):
      arr = []
      total = 0
      for i in range(0, n+1):
        if i % 13 == 0:
          arr.append(str(i))
      
      for i in arr:
        if ('4' in i) or ('7' in i):
          total = total + 1
      
      total1 = len(arr) - total 
      return total1 
      