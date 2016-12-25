
def product(s):
  #print s
  x = len([ a for a in s if a == '!'])
  y = len([ b for b in s if b == '?'])
  return x * y
  
  
product('') #0
product('!') #0
product('!!??!!') #8
