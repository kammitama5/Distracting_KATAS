def cat_mouse(x):
   counter = 0
   for i in x:
           if i == ".":
               counter = counter + 1
            
   if counter <= 3:
           return "Caught!"
   else:
           return "Escaped!"
		   
		   