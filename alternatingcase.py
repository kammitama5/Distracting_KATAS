def to_alternating_case(n):
    arr = []
    for i in n:
      if i == i.upper():
        c = i.lower()
        arr.append(c)
      else:
        c = i.upper()
        arr.append(c)
    g = ('').join(arr)
    return g
	
	