def word_search(query, seq):
    arr = []
    for i in seq:
      if query in i:
        arr.append(i)
    return arr
	
	