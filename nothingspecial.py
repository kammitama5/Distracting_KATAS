import re
def nothing_special(s):
      arr = []
      if type(s) != str:
        return "Not a string!"
      else:
          d = re.sub(r'([^\s\w]|_)+', '', s)
          return d
        
        
        #print re.sub("[^0-9a-zA-Z]", "" ,a)
      return
       