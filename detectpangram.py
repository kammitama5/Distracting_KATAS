import re
def is_pangram(s):
 
	b = s.replace(" ","")
    regex = re.compile('[^a-zA-Z]')
    c = regex.sub("", b)
    d = c.lower()
    e = ('').join(sorted(d))
    f = list(set(e))
    g = ('').join(f)
    alphabet = 'acbedgfihkjmlonqpsrutwvyxz'
    if alphabet in g:
      return True
    else:
      return False
    