
def to_binary(n):
    if n > 0:
        a = bin(n)
        return a[2:]
    elif n == 0:
        return "0"
    else:
        a = bin(n+(1<<32))
        return a[2:]                       
