def validate_pin(pin):
  #print len(pin)
  if (len(pin) == 4) | (len(pin) == 6):
    if all(char.isdigit() for char in pin):
      return "True"
    else:
      return "False"
  else:
    return "False"
  
  return
