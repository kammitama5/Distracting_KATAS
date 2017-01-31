def divisors(n):
    arr = []
    for i in range(1, n+1):
      if n % i == 0:
        g = i 
        arr.append(g)
    return len(arr)
	