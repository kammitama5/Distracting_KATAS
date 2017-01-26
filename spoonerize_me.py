def spoonerize(words):
    a = words.split(" ")
    x = a[0][0]
    y = a[1][0]
    return y + a[0][1:] +  " " + x + a[1][1:]
	