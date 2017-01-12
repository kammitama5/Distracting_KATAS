import re 
def capitals_first(string):
      arr = []
      arr1 = []
      
      a = string.split()
      for i in a:
        if i == i.title():
          a = arr.append(i)
        else:
          b = arr1.append(i)
      
      merged = arr + arr1
      sentence = (' ').join(merged)
      
      print sentence
  
      return 
    
    
    
    
capitals_first("sense Does to That Make you?") # "Does That Make sense to you?")
capitals_first("sense $23232 Does to That Make you?") # "Does That Make sense to you?")