def spinWords(sentence):
  sen = sentence.split()
  arr = []
  
  for i in sen:
      if len(i) > 4:
        w = i[::-1]
      else:
        w = i
      h = arr.append(w)
  arr1 = (' ').join(arr)
  return arr1
  