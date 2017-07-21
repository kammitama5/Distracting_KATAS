def WordsToMarks(String):
  total = 0
  word = list(String)
  
  for i in word:
    total = total + (ord(i) - 96)
    
   
  return total
  
  