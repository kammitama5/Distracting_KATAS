from collections import defaultdict
def find_most_frequent(l):
  
        x= defaultdict(int)
        if len(l) == 0:
          print []
        else:
          for i in l:
            x[i] += 1
          print x
          a = max(x, key=lambda i: x[i])
          print a
       
        
        
        
	      
        return

find_most_frequent([1, 1, 2, 3]) # set([1]), 'one most frequent element')
find_most_frequent([1, 1, 2, 2, 3])# set([1, 2]), 'two most frequent element')
find_most_frequent([])# set([]), 'empty')
