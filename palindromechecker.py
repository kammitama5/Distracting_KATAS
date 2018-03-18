def palindrome(word):
    word = ''.join([i for i in word if i.isalpha()])
    word = word.lower()
    #if len(word) < 3:
      #return False 
    if word == word[::-1]:
      return True 
    else:
      return False
	  