def sum_no_duplicates(l):
    arr = []
    total = 0
    for i in l:
     g = l.count(i)
     if g == 1:
       arr.append(i)
    
    for i in arr:
      total = total + i 
    return total
       