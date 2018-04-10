def minValue(ar):
    #try to write small
    a = sorted(list(set(ar)))
    b = ""
    for i in a:
      b = b + (str(i))
    return int(b)