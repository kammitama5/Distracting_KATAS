
def super_size(n):
    a = ' '.join(sorted(str(n)))
    b = a[::-1]
    c = b.replace(" ", "")
    d = int(c)
    return d
	
	