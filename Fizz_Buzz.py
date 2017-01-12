def solution(number):
  count = 0 # 15
  count1 = 0 # 3
  count2 = 0 # 5
  count3 = 0 # not used
  arr = []
  
  for i in range(0, number):
  
    if (i % 15 == 0):
      count = count + 1
    elif (i % 3 == 0):
      count1 = count1 + 1 
      b = count1 
      #print b
    elif (i % 5 == 0):
      count2 = count2  + 1
      #print c
    else:
      count3 = count3 + 1
      d = count3
  a =  count1 
  b =  count2
  c =  count -1

  arr.append(a)
  arr.append(b)
  arr.append(c)

  return arr
  
  