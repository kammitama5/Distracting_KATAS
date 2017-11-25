def maxDifference(startVal, endVal):
    arr = []
    for i in range(startVal,endVal + 1):
     if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           arr.append(i)
    try:
      last = arr[-1]
      first = arr[0]
      diff = last - first
      return diff
    except:
      return 0
           
maxDifference(2, 5)#3
maxDifference(2,2)#0
maxDifference(24, 28)#0
