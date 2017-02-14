def largest_factor(num1, num2):
    arr1 = []
    arr2 = []
    
    
    for i in range(1, num1+1):
      if num1 % i == 0:
        arr1.append(i)
    for i in range(1, num2+1):
      if num2 % i == 0:
        arr2.append(i)

    
    c = list(set(arr1) & set(arr2))
    c1 = c[-1]
    
    
    return c1
  