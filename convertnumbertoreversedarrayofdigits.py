def digitize(n):
  strlist = str(n)
  reverse_strlist = (strlist[::-1])
  #return reverse_strlist
  arr = [int(x) for x in str(reverse_strlist)]
  return arr