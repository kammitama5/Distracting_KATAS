def map(function, iterable):
    arr = []
    for i in iterable:
        g =  function(i)
        arr.append(g)
    return arr
	