def changer(string):
    arr = []
    x =  list(string)
    for i in x:
      if i == " " or i.isdigit():
        a = i
        arr.append(a)
      elif ((i.isalpha())):
        a = chr(ord(i)+1)
        if ((a == "a") or (a == "e") or (a == "i") or (a == "o") or (a == "u") or (a == "A") or (a == "E") or (a == "I") or (a == "O") or (a == "U") or (a == " ")):
          a = a.upper()
          arr.append(a)
        else:
          a = a.lower()
          arr.append(a)

    print ('').join(arr)
    return
     