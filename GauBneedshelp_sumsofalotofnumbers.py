def f(n):
    counter = 0
    if type(n) != int:
        return None
    elif n <= 0:
        return None
    else:
        for i in range (n+1):
            counter = counter + i
        return (counter)