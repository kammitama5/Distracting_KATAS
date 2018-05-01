def max_number(n):
    a = sorted(str(n))[::-1]
    b = ''.join(a)
    return int(b)
    