def consonant_count(s):
   consonants = list("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
   num = sum(s.count(c) for c in consonants)
   
   return num
   