def count0(n):
    arr = ""
    count = 0
    for i in range(1, n+1):
        arr += str(i)
    list1 = list(arr)
    for i in list1:
      if i == "0":
        count += 1 
    return count
    