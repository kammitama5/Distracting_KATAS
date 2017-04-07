def reverse_alternate(string):
      a = string.split()
 
      arr = []
      for i in a:
        if a.index(i) % 2 == 0:
          arr.append(i)
        else:
          arr.append(i[::-1])
          
      return (' ').join(arr)
	  
	  