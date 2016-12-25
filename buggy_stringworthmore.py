import unicodedata

def highest_value(a, b):
    #print(a, b)
    a1  = a.lower().upper()
    b1 = b.lower().upper()
    counter1 = 0 
    counter2 = 0 
    for i in a1:
      counter1  += counter1 + ord(i)
    #print counter1
    for j in b1:
      counter2 += counter2 + ord(j)
    #print counter2
    if counter1 == counter2:
      print a
      print counter1, counter2
    elif counter1 > counter2:
      print a
      print counter1, counter2
    else:
      print b
      print counter1, counter2
      

    
highest_value("ABCD", "DCBA")  
highest_value("b", "a")
highest_value("a", "a")
highest_value("a", "b")
highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567") # "KkLlMmNnOoPp4567"