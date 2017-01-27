def collatz(n):
    arr = [n]
    arr1 = []
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            arr.append(n)
        else:
            n = int(3 * n + 1)
            arr.append(n)
    
    for i in arr:
      b = str(i)
      arr1.append(b)
    c = ('->').join(arr1)
    return c
	