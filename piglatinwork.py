def pig_it(text):
  #print text
  w = text.split()
  arr = []
  r = 'ay'
  for i in w:
     arr.append(i[1::] + i[0] )
  #print arr
  for i in arr:
    if i.isalpha:
      arr1 = [x + r for x in arr]
    else:
      arr1 = x
  #arr1 = [x + r for x in arr]
  return ' '.join(arr1)