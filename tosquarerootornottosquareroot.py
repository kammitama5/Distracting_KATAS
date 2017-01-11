import math
def square_or_square_root(arr):
    arr1 = []
    for i in arr:
      if (math.sqrt(i) == int(math.sqrt(i))):
        a = int((math.sqrt(i)))
        arr1.append(a)
      else:
        a = i * i
        arr1.append(a)
    return arr1
	
	