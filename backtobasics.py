def types(x):
    try:
      a = ((type(x)))
      return a[7:-2]
        
    except:
      return str(type((x)))[8:-2]
	  