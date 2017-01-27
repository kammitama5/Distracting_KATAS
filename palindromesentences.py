def is_palindrome_sentence(s):
      arr = []
      for i in s:
        if i.isalpha():
          b = i.lower()
          arr.append(b)
      x = ('').join(arr)
      y = x[::-1]
      if x == y:
        return True
      else:
        return False
      return
	  
	  