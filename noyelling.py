def filter_words(st):
   a = st[0].title() + st[1:].lower()
   r = a.split()
   return (' ').join(r)
   