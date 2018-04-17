def max_tri_sum(numbers):
    num = sorted(numbers)
    a = sorted(set(num))[::-1] 
    b = a[0]
    c = a[1]
    d = a[2]
    return (b + c + d)