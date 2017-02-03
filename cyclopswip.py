def cyclops (n):
    a = bin(n)[2:]
    #print a
    b = len(a) / 2 
    c = a[b]
    d = a[:(b)] + a[(b+1):]
    e = list(d)

    
    if ((c == '0') and (len(d) % 2 == 0) and (len(set(e)) == 1)):
      return True
    else:
      return False
	  