def square_digits(num):
  string = str(num)
  h = list(string)
  arr = []
  for i in h:
    arr.append(str(int(i) * int(i))) 
  p = ('').join(arr)
  return int(p)
  
  