def sum_of_integers_in_string(s):
   import re
   total = 0
   g = re.findall(r'\d+', s)
   for i in g:
       total = total + int(i)
   return total
   