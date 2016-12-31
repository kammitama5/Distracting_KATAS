def pig_it(text):
      arr = []
      
      y = text.split()
      
      for i in y:
            if i.isalpha():
              arr.append(i[1::] + i[0] + ('ay') )
            else:
              arr.append(i)
            
      
      final = (' ').join(arr)
      return final
	  
	  