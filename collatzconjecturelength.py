def collatz(n):
    arr = []
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            arr.append(n)
        else:
            n = int(3 * n + 1)
            arr.append(n)
    else:
       return len(arr) + 1
        