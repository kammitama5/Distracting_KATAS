def find_average(nums):
    counter = 0
    length = len(nums)
    if length == 0:
        return 0 
    else:
      for i in nums:
        counter = counter + i 
        
    return ((counter * 100.0) / 100.0) / length
    
    
find_average([5, 7, 3, 7]) # 5.5)

