def sum_array(arr):
  arr.sort()
  if len(arr) < 1:
    return 0
  n = 1
  del arr[-n:]
  del arr[0]
  print sum(arr)
 


sum_array([6, 2, 1, 8, 10]) # 16)
sum_array([6, 0, 1, 10, 10]) # 17)
sum_array([-6, -20, -1, -10, -12]) # -28)
sum_array([-6, 20, -1, 10, -12]) # 3)