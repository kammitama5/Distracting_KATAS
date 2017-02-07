def reverse_invert(lst):
     arr = []
     arr1 = []
     arr2 = []
     for i in lst:
       if type(i) == int:
         arr.append(str(i)[::-1])
     for i in arr:
       if i[-1] == '-':
         i = '-' + i[:-1] 
         arr1.append(i)
       else:
         arr1.append(i)
     for i in arr1:
       g = int(i)
       h = 0 - g
       arr2.append(h)
     return arr2
	 