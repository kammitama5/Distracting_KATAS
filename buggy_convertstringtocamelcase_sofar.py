import re

def to_camel_case(string):

  w = filter(None, re.split("([A-Z][^A-Z]*)", string))
  p = (" ").join(w)
  
  # only capitalize [:1] and onwards..first letter keeps ! capitalization
  a = re.sub(r'\W+', ' ', p)
  print a
  
  a1 = a.title()
  b = re.compile('[-_]')
  c = b.sub('', a1)
  d = c.split()
  e =("").join(d)
  return e
  
  return
  
to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")

