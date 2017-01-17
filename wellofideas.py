def well(x):
        count = 0  #bad
        count1 = 0 #good
        count2 = 0 #other

        for i in x:
          if i == 'bad':
            count = count + 1 
            
          elif i == 'good':
            count1 = count1 + 1
           
          else:
            count2 = count2 + 1

        if count1 > 2:
          return "I smell a series!"
        elif ((count1 == 1) or (count1 == 2)):
          return "Publish!"
        elif (count1 == 0):
          return "Fail!"
        else:
          return None
		  
		  