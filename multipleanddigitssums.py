def procedure(i):
        total = 0
        arr = []
        for j in range(i, 100+1):
          if j % i == 0:
            arr.append(str(j))
        a = ''.join(arr)
        b = list(a)
        for i in b:
          total = total + int(i)
        #print total
    
        return total
		
		