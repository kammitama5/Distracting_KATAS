def largestPower(N):
  import math
  num = 0
  #g = (math.pow(3, num))
  while (math.pow(3, num) < N):
    num = num + 1 
  return num - 1
    