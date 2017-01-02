def median(arr):
    arr1 = sorted(arr)
    if int(len(arr1) == 1):
        return arr1[0]
    elif int(len(arr1) % 2 == 0):
        n1 = int(len(arr1) / 2)
        return ((arr1[n1] + arr1[n1 - 1]) / 2.0)
    else:
        n = int(len(arr1) / 2)
        return arr1[n]