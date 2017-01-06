def lowest(*days):
      
      a = days[0]
      b = days[1]
      c = days[2]
      
      a1 = sorted(a, key=int)
      b1 =sorted(b, key=int)
      c1 = sorted(c, key=int)

      a2 = a1[0]
      b2 = b1[0]
      c2 = c1[0]
      
      mylist = []
      mylist.append(a2)
      mylist.append(b2)
      mylist.append(c2)
      
      return mylist
	  
	  