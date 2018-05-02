def max_product(a):
    a1 = sorted(set(a))[::-1]
    x = a1[0]
    y = a1[1]
    w = x * y
    return w
	## This was neat because sorted below time limit once removed dupes