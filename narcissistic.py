def narcissistic( value ):
  strvalue = str(value)
  n = len(strvalue)
  total = 0
  for i in strvalue:
    total = total + (int(i) ** n)
  if total == value:
    return True
  else:
    return False