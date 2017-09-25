def solve(a):
    arr = []
    odds = 0
    evens = 0
    for i in a:
      try:
        if (i == int(i)):
          if i % 2 == 0:
            evens = evens + 1
          elif i % 2 == 1:
            odds = odds + 1
      except:
        arr.append(i)
    diff = evens - odds 
    return diff 
