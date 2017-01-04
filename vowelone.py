def vowel_one(s):
      a = []
      for i in s:
         if ((i == "a") or (i == "e") or (i == "i") or 
         (i == "o")
         or (i == "u") or (i == "A") or (i == "E") or (i == "I")
         or (i == "O") or (i == "U")):
           a.append("1")
         else:
           a.append("0")
           
      b = ''.join(a)
      return b
           