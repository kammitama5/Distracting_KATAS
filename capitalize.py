def capitals(word):
      arr = []
  
      for i in word:
        if i.isupper():
          a = word.index(i)
          arr.append(a)
          
      return arr
          
  
  
      return 
    
    
    
    
capitals('CodEWaRs') # returns [0, 3, 4, 6]

