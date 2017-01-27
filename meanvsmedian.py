def mean_vs_median(numbers):
    a = int(len(numbers)/2)
    
    x = sorted(numbers)[a]
    count = 0
    leng = len(numbers)
    for i in numbers:
      count = count + i
    y = count / leng
    
    if x > y:
      return "median"
    elif y > x:
      return "mean"
    else:
      return "same"
	  