def tacofy(word):
    arr = []
    arr.append("shell")
    for i in word.lower():
      if i == 'a':
        arr.append('beef')
      elif i == 'e':
        arr.append('beef')
      elif i == 'i':
        arr.append('beef')
      elif i == 'o':
        arr.append('beef')
      elif i == 'u':
        arr.append('beef')
      elif i == 't':
        arr.append("tomatoe")
      elif  i == 'l':
        arr.append("lettuce")
      elif i == 'c':
        arr.append("cheese")
      elif i == 'g':
        arr.append('guacamole')
      elif i == 's':
        arr.append('salsa')
    arr.append("shell")
    return arr
	