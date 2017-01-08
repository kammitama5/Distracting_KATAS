def pig_latin(word):
   if len(word) <= 3:
       return word
   else:
       word1 = word[1::]
       return word1 + word[0] + 'ay'
	   
	   