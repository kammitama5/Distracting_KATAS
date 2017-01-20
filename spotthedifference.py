def spot_diff(s1, s2):
     list1 = list(s1)
     list2  = list(s2)
     
     arr = []
     arr1 = []
     
     for w in list1:
       d = list1.index(w)
       arr1.append(d)
       
     for i in list1:
       for j in list2:
         if i == j:
           c = list1.index(i)
           arr.append(c)
 
     
     listC = [item for item in arr1 if item not in arr]
     return listC
     