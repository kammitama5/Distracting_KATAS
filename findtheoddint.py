from collections import Counter
def find_it(seq):
      a = Counter(seq)
      x = a.keys()
      y =  a.values()
      for i in y:
        if i % 2 != 0:
          g = i
          
      return a.keys()[a.values().index(g)]
	  