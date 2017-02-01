def are_coprime(n,m):
    arr = []
    arr1 = []
    for i in range(1, n+1):
      if n % i == 0:
        arr.append(i)
    
    for j in range(1, m+1):
      if m % j == 0:
        arr1.append(j)
    
    inters = list(set(arr).intersection(arr1))
    if len(inters) == 1:
      return True
    else:
      return False
	  