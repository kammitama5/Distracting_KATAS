def invert(lst):
    arr = []
    if lst == []:
        return []
    else:
        for i in lst:
            g = 0 - i 
            arr.append(g)
        return arr
		