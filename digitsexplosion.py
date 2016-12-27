def explode(s):
    #print s
    arr = []
    string = ""
    for i in s:
      if i == "0":
        #print ""
        arr.append("")
      if i == "1":
        #print i
        arr.append(i)
      if i == "2":
        #print i * 2
        arr.append(i * 2)
      if i == "3":
        #print i * 3
        arr.append(i * 3)
      if i == "4":
        #print i * 4
        arr.append(i * 4)
      if i == "5":
        #print i * 5
        arr.append(i * 5)
      if i == "6":
        #print i * 6 
        arr.append(i * 6)
      if i == "7":
        #print i * 7
        arr.append(i * 7)
      if i == "8":
        #print i * 8
        arr.append(i * 8)
      if i == "9":
        #print i * 9 
        arr.append(i * 9)
    #print arr
    arr1 = ('').join(arr)
    print arr1
    return
  
  
  
explode("312") # returns 333122
explode("102269") #"12222666666999999999"
explode("0") # returns ""
explode("000") # returns ""
explode("123") # returns "122333"