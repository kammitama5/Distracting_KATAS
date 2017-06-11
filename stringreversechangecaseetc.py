def reverseAndMirror(s1,s2):
    s_ = []
    s3 = list(s1)
    for i in s3:
      if i == i.upper():
        s_.append(i.lower())
      else:
        s_.append(i.upper())
    s = ('').join(s_)
    srev = s[::-1]
    
    s4 = []
    s5 = list(s2)
    for i in s5:
      if i == i.upper():
        s4.append(i.lower())
      else:
        s4.append(i.upper())
    first = ('').join(s4)
    head1 = first[::-1]
    
    final = head1 + '@@@' + srev + s 
    return final
	