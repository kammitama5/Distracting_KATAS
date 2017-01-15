def reverse_slice(s):
    b = s
    a = list(b)
    count = ""
    arr = []
    
    for i in range(0, len(a)):
       count = (count + a[i])
       e = count[::-1]
       arr.insert(0, e)
    return arr
	
	