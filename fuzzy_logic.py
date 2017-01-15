def fun(n):
    
    a = dict((i, n.count(i)) for i in n)
    find1 = 1
    for key in a.keys():
          if a[key] == find1:
            return key
			