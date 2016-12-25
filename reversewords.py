def reverse_words(str):
  str1 = str.split(" ")
  #print str1
  arr = []
  for i in str1:
     arr.append(i[::-1])
  #print arr
  arr1 = " ".join(arr)
  return arr1
  
  
  
  


reverse_words('This is an example!') #'sihT si na !elpmaxe'

