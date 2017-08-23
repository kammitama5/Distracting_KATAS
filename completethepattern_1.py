def pattern(n):
    arr = ""
    if n < 1:
      return ""
    elif n == 1:
      return "1"
    else:
      for i in range(2, n+1):
        arr =  arr + "\n" + str(i) * (i)
    return "1" + arr
	