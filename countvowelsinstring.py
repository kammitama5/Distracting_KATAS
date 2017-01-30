def count_vowels(s = ''):
      if type(s) == str:
        a = s.lower()
        b = list(a)
        count = 0
        for i in b:
          if (i == 'a'):
            count = count + 1 
          elif (i == 'e'):
            count = count + 1 
          elif (i == 'i'):
            count = count + 1 
          elif (i == 'o'):
            count = count + 1
          elif (i == 'u'):
            count = count + 1
          else:
            count = count 
        return count
      else:
        return None
		