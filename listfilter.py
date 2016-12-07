def filter_list(l):
  mynewlist = []
  anotherlist = []
  for i in l:
    try:
      int(i)
      if type((i)) != str:
        (mynewlist.append(i))
     
    except ValueError:
        if i.isdigit():
          anotherlist.append(i)
          
  return mynewlist

