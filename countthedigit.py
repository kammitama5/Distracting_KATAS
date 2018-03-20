def nb_dig(n, d):
    import re
    a = ""
    for i in range(0,n+1):
      a = a + str(i*i)
    b = list(a)
    count = 0
    for i in b:
      if i == str(d):
        count = count + 1 
    return count
    