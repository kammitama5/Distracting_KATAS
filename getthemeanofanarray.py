def get_average(marks):
  total = 0
  counter = 0
  for i in marks:
    counter = counter + 1
    total = total + i
  return total / counter
    
  
  
  
  
  
get_average([2, 2, 2, 2]) # returns 2
get_average([1, 5, 87, 45, 8, 8]) # returns 25
get_average([2,5,13,20,16,16,10]) # returns 11
get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]) # returns 11


