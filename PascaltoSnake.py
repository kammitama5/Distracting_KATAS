import re

def to_underscore(string):
  w = filter(None, re.split("([A-Z][^A-Z]*)", string))
  p = ("_").join(w)
  a = p.lower()
  return str(a)