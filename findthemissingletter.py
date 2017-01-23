def find_missing_letter(chars):
          count = 0
          count1 = 0

          for i in chars:
            count = count + ord(i) 

          begin = chars[0]
          end = chars[-1]

          for i in range(ord(begin), ord(end)+1):
            count1 = count1 + i 

          
          diff = count1 - count 
          return chr(diff) 
          return
		  