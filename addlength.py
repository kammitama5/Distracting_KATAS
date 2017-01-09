def add_length(str_):
      arr = []
      a = str_.split()
      for i in a:
        b = i + " " + str(len(i))
        arr.append(b)
      return arr
	  
	  