import re
def remove(s):
            count = 0
            for i in s:
              if i == '!':
                count = count + 1
            
            a = re.sub(r'([^\s\w]|_)+', '', s)
        
            return a + (count * '!')
          
            return
          
          




remove("Hi!") #=== "Hi!"
remove("Hi! Hi!") #=== "Hi Hi!!"
remove("Hi! Hi! Hi!") #=== "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") #=== "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") #=== "Hi Hi Hi!!!!"