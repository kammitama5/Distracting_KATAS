# Find the smallest integer in an array

def findSmallestInt(arr):
  arr.sort()

  print(arr[0])
  
  
  
  
findSmallestInt([78,56,232,12,11,43]) # returns 11
findSmallestInt([78,56,-2,12,8,-33]) # returns -33
findSmallestInt([34, 15, 88, 2]) # returns 2
findSmallestInt( [34, -345, -1, 100]) # returns -345