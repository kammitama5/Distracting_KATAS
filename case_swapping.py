def swap(string_):
    arr = []
    for i in string_:
      if i.isupper():
        b = i.lower()
        arr.append(b)
      else:
        b = i.upper()
        arr.append(b)

    c = ('').join(arr)
    return c
  