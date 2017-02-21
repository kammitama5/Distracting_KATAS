def is_palindrome(s):
    arr = []
    if s == None:
      return False 
    else:
      a = s.lower()
      for i in a:
        if i.isalpha() or i.isdigit():
          arr.append(i)
        b = ('').join(arr)
      if b == b[::-1]:
        return True 
      else:
        return False
		