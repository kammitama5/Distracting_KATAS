import re
def evenator(s):
    arr = []
    a = re.sub(r'([^\s\w]|_)+', '', s)
    b = a.split(' ')
    for i in b:
      if ((len(i)) % 2 == 1):
        c = i + i[-1]
        arr.append(c)
      else:
        arr.append(i)
    d = (' ').join(arr)
    return d.rstrip()