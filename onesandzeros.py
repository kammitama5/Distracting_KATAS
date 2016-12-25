def binary_array_to_number(arr):
  arrr = list(arr)
  arr1 = ('').join(str(i) for i in arrr)
  return int(arr1, 2)
