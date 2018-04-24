def max_multiple(divisor, bound):
    arr = []
    for i in range(1, bound+1):
        if i % divisor == 0:
            arr.append(i)
    a = sorted(arr)[::-1]
    if len(a) > 0:
        return a[0]
    else:
        return 0