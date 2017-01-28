def alternate_sq_sum(arr):
    a = arr
    count = 0
    for i in a:
      if ((a.index(i) % 2) == 0):
        count = count + i
        print i 
        print count
      elif ((a.index(i) % 2) != 0):
        count = count + (i * i)
        print i
        print count
      else:
        print i
    #print count
    return arr
    
    
#alternate_sq_sum([11, 12, 13, 14, 15]) #should return 379
alternate_sq_sum([13, 11, 8, 11, 7, 8, 14, 11, 6, 11, 10, 13, 15, 9, 11, 14])

#1078