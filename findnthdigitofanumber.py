def find_digit(num, nth):
    num = abs(num)
    if nth <= 0:
      return -1
    if nth > 0 and nth > len(str(num)):
      return 0 
    else:
      s = str(num)
      l = len(s)
      letter = s[l-nth]
      return int(letter)
      