def freq_seq(s, sep):
    arr = []
    str1 = ""
    for i in s:
      arr.append(s.count(i))
    for j in arr:
      str1 = str1 + (str(j) + sep)
    b =  str1[:-1]
    return b
	
	