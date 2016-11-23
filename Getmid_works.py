def get_middle(s):
  #if (len(s) == 1):
   # print(s)
  if (len(s) % 2 == 0):
    arger = len(s) / 2
    arger, arger1 = s[:len(s)/2],s[len(s)/2:]
    w=arger1
    u=arger
    q = str(u[-1])+str(w[0])
    return(q)
  else:
    arger3 = len(s)
    arger4 = arger3 / 2
    return(s[arger4])
  return



get_middle("test") # should return "es"
get_middle("testing") # should return "t"
get_middle("middle") # should return "dd"
get_middle("A") # should return "A"
get_middle("of") # should return "of"