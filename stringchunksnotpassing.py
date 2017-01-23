import re
def string_chunk(string, n):
     
      if n > len(string):
        arr = []
        arr.insert(0, string)
        return arr
      
      else:
        n1 = '.' * n + '?'
        a =re.findall(n1, string)
        return a
      return
  

