def show_sequence(n):
    arr = []
    count = 0
    if n > 0:
      for i in range(0, n+1):
        count = count + i
        arr.append(str(i))
      x = ('+').join(arr) + ' ' + '=' + ' ' + str(count) 
      return x
    elif n == 0:
      return "0=0"
    else:
      return str(n)+'<0'
	  