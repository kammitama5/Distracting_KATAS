def initializeNames(name):
  
      a = name.split()
      arr = []

      if (len(a) == 1):
        return (' ').join(a)
      elif (len(a) == 2):
        b = (' ').join(a)
        return b
      else:
        c = a[1:-1]
        for i in c:
          d = i[0] + "."
          arr.append(d)
        j = (' ').join(arr)
        return  a[0] + " " + j + " " + a[-1]
		
		