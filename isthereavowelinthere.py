def is_vow(inp):
    arr = []
    for i in inp:
        if ((i == 97) or  (i == 101) or (i == 105) or (i == 111) or (i == 117)):
            arr.append(chr(i))
        else:
            arr.append(i)
    return arr
	
	