def remove(s):
    if len(s) <= 1:
      return s 
    else:
      if s[-1] == "!":
        a = s[:-1]
        return a 
      else:
        return s
      