def sum_of_n(n):
      arr = []
      count = 0
      if n >= 0:
        for i in range(0, n+1):
          count = count + i
          arr.append(count)
        return arr
      else:
        w = abs(n)
        for i in range(0, w+1):
          count = count + abs(i)
          arr.append(count * (-1))
        return arr
		