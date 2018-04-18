def balanced_num(number):
    a = str(number)
    if len(a) <= 2:
      return "Balanced"
    elif len(a) % 2 == 0:
      
      mid = a[int(len(a) / 2)-1] + a[int(len(a) / 2)]
      left = a[0:int(len(a) / 2)-1]
      right = a[int(len(a) / 2)+1::]
      sum1 = 0 
      sum2 = 0
      for i in left:
        sum1 = sum1 + int(i)
      for j in right:
        sum2 = sum2 + int(j)
      if sum1 == sum2:
        return "Balanced"
      else:
        return "Not Balanced"
    else:
      mid = a[int(len(a) / 2)]
      left = a[0:int(len(a) / 2)]
      right = a[int(len(a) / 2)+1::]
      sum1 = 0 
      sum2 = 0
      for i in left:
        sum1 = sum1 + int(i)
      for j in right:
        sum2 = sum2 + int(j)
      if sum1 == sum2:
        return "Balanced"
      else:
        return "Not Balanced"
    return
	