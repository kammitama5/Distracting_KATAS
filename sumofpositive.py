def positive_sum(arr):
    counter = 0
    for i in arr:
        if i > 0:
            counter += i
    return counter