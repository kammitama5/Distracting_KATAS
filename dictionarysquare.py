def dict_square(numbers):
    arr = []
    arr1 = []
    dict1 = {}
    for i in numbers:
      arr.append(i)
      arr1.append(numbers[i] * numbers[i])
    for i in range(len(arr)):
      dict1[arr[i]] = arr1[i]
  
    return dict1
  