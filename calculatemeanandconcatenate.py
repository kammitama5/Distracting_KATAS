def mean(lst):
  wonder = ""
    #print lst
  for char in lst:
    if char.isalpha():
      wonder += char
  #print wonder
  
  counter = 0
  total = 0
  for i in lst:
    if i.isdigit():
      total += int(i)
      counter += 1
  #print ((total * 100.0) / 100.0)
  #print ((counter * 100.0) / 100.0)
  bread = ((total * 100.0) / 100) / ((counter * 100.0) / 100)
  
  #print bread
  array = []
  array.append(bread)
  array.append(wonder)
  return array