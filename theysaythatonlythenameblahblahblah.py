def is_opposite(s1,s2):
      arr = ""
      if (s1 == "") or (s2 == ""):
        return False
      else:
        for i in s1:
          if i.isupper():
            c = i.lower()
            arr = arr + c
          else:
            c = i.upper()
            arr = arr + c

        if arr == s2:
          return True
        else:
          return False
		  
		  