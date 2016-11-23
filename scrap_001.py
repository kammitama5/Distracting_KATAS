def get_middle(s):
  
  # if case is one letter
  print(s)
  
  # if test case is odd
  arger3 = len(s)
  arger4 = arger3 / 2
  #print(arger3)
  #print(arger4)
  #print(s[arger4])
  
  #=============#
  
  # if test case is even
  arger = len(s) / 2
  arger, arger1 = s[:len(s)/2],s[len(s)/2:]
  w = arger1
  u = arger
  #print arger
  #print arger1
  #print(u)
  #print(w)
  
  #print arger[:-1]
  #print arger1[0]
  q = str(u[-1])+str(w[0])
  #print(q)
  
  
  
  return



#get_middle("test") # should return "es"
get_middle("testing") # should return "t"
#get_middle("middle") # should return "dd"
#get_middle("A") # should return "A"
#get_middle("of") # should return "of"