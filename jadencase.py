def toJadenCase(string):
    
    list1 = [a[0].upper() + a[1:] for a in string.split()]
    b = (' ').join(list1)
    return b
	