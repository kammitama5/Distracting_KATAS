import numpy as np

def is_isogram(string):
  w = list(string)
  q = [element.upper() for element in w]
  print(w)
  if len(w) != len(set(w)):
    #print("True")
    return False
  if len(q) != len(set(q)):
    return False
  else:
    #print("False")
    return True