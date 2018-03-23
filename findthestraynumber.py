def stray(arr):
    g = 0
    for i in arr:
        if arr.count(i) % 2 != 0:
            g = i
    return g