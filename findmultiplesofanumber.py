def find_multiples(integer, limit):
    arr = []
    for i in range(integer, limit+1, integer):
        arr.append(i)
    return arr
	
	