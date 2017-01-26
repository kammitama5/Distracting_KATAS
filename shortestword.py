def find_short(s):
    arr = []
    a = s.split(" ")
    for i in a:
      g = len(i)
      arr.append(g)
    return min(arr)
	