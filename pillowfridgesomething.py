import re
def pillow(s):
    count = 0
    first = s[0]
    second = s[1]
    char1 = 'n'
    char2 = 'B'
    
    b = [n for (n, e) in enumerate(first) if e == char1]
    c = [m for (m, f) in enumerate(second) if f == char2]
    
    #print b, c
    d = b + c 
    #print d 
    
    for i in b:
      for j in c:
        if i == j:
          count = count + 1
    if count >= 1:
      return True
    else:
      return False
    