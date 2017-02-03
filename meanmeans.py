import math
def geo_mean(nums, arith_mean):
      
      a = len(nums) + 1 
      last = (a * arith_mean) - (sum(nums))
      product = 1 
      nums.append(last)
      x1 = len(nums)
      
      for i in nums:
        product = product * i 
      
      x = product 
      y = product ** (1.0/x1)
      return y
	  