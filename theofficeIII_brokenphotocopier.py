def broken(inp):
    arr = []
    a = ('').join(inp)
    b = list(a)
    
    for i in b:
      if i == "0":
        arr.append("1")
      else:
        arr.append("0")
    c = ('').join(arr)
    return c
	