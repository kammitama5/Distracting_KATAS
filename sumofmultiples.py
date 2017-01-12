def sum_mul(n, m):
    count = 0
    if ((n <= 0) or (m <= 0)):
        return "INVALID"
    else:
      for i in range(n, m):
        if (i % n == 0):
          count = count +  i
      return count
    