def find_GCF(a, b):
    arr = []
    arr1 = []
    for i in range(1, a+1):
      if a % i == 0:
        g = i
        arr.append(g) 
    for j in range(1, b + 1):
      if b % j == 0:
        h = j 
        arr1.append(h)

    x1 = set(arr)
    x2 = set(arr1)
    x = x1.intersection(x2)
    y = list(x)
    y1 = sorted(y)
    return y1[-1]
	