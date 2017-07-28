def listAvg(arr):
    total = 0.0
    a = len(arr) * 1.0
    for i in arr:
        total = total + i
    return (total / a)
