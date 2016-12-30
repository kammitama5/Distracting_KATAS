import re 

def is_palindrome(s):
    if type(s) != str:
      return False
    else:
        q = s.lower()
        w = q.split()
        q = ''.join(w)
        q1 = re.sub(r'\W+', '', q)
    
    
        if q1[::-1] == q1:
           return True
        else:
          return False
		  
		  