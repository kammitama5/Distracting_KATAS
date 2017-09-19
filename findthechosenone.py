def find_uniq(arr):
# find all unique items
  a = list(set(arr))
  # find count of unique item in orig list
  for i in a:
  # if count of item is 1, that is unique item
    if arr.count(i) == 1:
      return i
	  
	  