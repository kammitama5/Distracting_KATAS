def swap(st):
    arr = []
    s = list(st)
    for i in s:
      if i == 'a':
        arr.append('A')
      elif i == 'e':
        arr.append('E')
      elif i == 'i':
        arr.append('I')
      elif i == 'o':
        arr.append('O')
      elif i == 'u':
        arr.append('U')
      else:
        arr.append(i)
    return ''.join(arr)
