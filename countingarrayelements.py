def count(array):
   m =  dict((x,array.count(x)) for x in set(array))
   return m
   
   