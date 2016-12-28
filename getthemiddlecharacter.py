def get_middle(s):
   # length word 2 or less
    if (len(s) <= 2):
      return s
    # length word even
    elif (len(s) % 2 == 0):
      w = (len(s) / 2) 
      w2 = w - 1 
      return s[w2] + s[w]
    # lenth word odd
    
    else:
      w1 = (len(s) / 2)  
      return s[w1]