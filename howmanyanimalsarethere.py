def CountAnimals(sentence):
    arr1 = []
    arr =  sentence.split(" ")
    total = 0;
    total1 = 0;
    for i in arr:
     try:
       int(i)
       total = total + int(i)
       arr1.append(total)
     except:
       total = 0
    if len(arr1) == 0:
      return 0
    else:
      for i in arr1:
        total1 = total1 + i 
      return total1
	  
	  