import re 

def kebabize(string):
  #print string
  # split at upper
  x = ' '
  y = ''.join(x + w if w.isupper() else w for w in string).strip(x).split(x)
  #print y
  for item in y:
    if item.isdigit():
      y.remove(item)
  #print y
  c = str(y)
  from string import digits
  d = c.translate(None, digits)
  e = d.lower()
  f = e.split()
  g = ''.join(f)
  print g
  
  