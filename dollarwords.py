def dollar_word(input_word):
    a = list(input_word.lower())
    count = 0
    for i in a:
      count = count + (ord(i) - 96)
    if (count == 100):
      return True
    else:
      return False
	  