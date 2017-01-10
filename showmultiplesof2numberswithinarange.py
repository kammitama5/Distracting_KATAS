def multiples(s1, s2, s3):
    arr = []
    for i in range(s1, s3):
      if ((i % s1 == 0) and (i % s2 == 0)):
        a = i
        arr.append(a)
    return arr
	
	