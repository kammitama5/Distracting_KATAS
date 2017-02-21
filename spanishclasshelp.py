def gender(*nouns):
    arr = []
    arr1 = []
    #print nouns
    for i in nouns:
      b = i
      arr.append(b)

    
    for i in arr:
      if i == None:
        c = None
        arr1.append(None)
      elif type(i) == int:
        c = i
        arr1.append(c)
      else:
        if i[-1] == 'o':
          c = 'el ' + i 
          arr1.append(c)
        elif i[-1] == 'a':
          c = 'la ' + i 
          arr1.append(c)
        elif i[-2:] == 'os' or i[-2:] == 'es':
          c = 'los ' + i 
          arr1.append(c)
        elif i[-2:] == 'as':
          c = 'las ' + i 
          arr1.append(c)
        elif i[-1] == 's':
          c = 'los ' + i
          arr1.append(c)
        else:
          c = 'el ' + i 
          arr1.append(c)
          
    return arr1
        