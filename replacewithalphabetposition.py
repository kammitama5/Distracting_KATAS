def alphabet_position(text):
    arr = []
    a = text.lower()
    for i in a:
        x = (ord(i)) - 96
        if x >= 0:
            arr.append(x)
    a = arr 
    b = " ".join(str(x) for x in a)
    return b
	
	