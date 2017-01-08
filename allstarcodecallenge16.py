def no_repeat(string):
    arr = []
    for i in string:
      if string.count(i) <= 1:
        b =  i
        arr.append(b)
    return arr[0]
	