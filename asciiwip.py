def compare(s1,s2):
      total = 0;
      total1 = 0;
      a = s1.upper()
      b = s2.upper()
      a1 = list(a)
      b1 = list(b)
      for i in a1:
        total = total + ord(i)
      for j in b1:
        total1 = total1 + ord(j)
      #print total, total1
      
      if total == total1:
        print True
      else:
        print False
      return
	  
	  