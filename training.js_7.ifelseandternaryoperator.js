def sale_hotdogs(n):
    if (n < 5):
        a = 100 * n
    elif (n >= 5) and (n < 10):
        a = 95 * n
    elif (n >= 10):
        a = 90 * n
    else:
        a = n
    return a
	