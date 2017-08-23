def first_non_consecutive(arr):
    #print arr 
    arr1 = []
    arr2 = []
    a = arr[0]
    b = arr[-1]
    for i in range(a, b+1):
      arr1.append(i)
    #print arr1
    d = list(set(arr1) - set(arr))
    e = sorted(d)
    try:
      return e[0]+1
    except:
      return None
	  