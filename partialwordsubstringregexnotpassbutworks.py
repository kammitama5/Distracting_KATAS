import re
def word_search(query, seq):
    arr = []
    for i in seq:
      if re.search(query, i):
        arr.append(i)
    return arr
    
    return
	