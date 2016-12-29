def rain_amount(mm):
      
     if (rain_amount < 40):
         print "You need to give your plant " + {rain_amount - 40} + "mm of water"
    else:
         print "Your plant has had more than enough water for today!"
         
         
         
rain_amount(100) # "Your plant has had more than enough water for today!")
rain_amount(40) # "Your plant has had more than enough water for today!")
rain_amount(39) # "You need to give your plant 1mm of water")
rain_amount(5) #"You need to give your plant 35mm of water")
rain_amount(0) #"You need to give your plant 40mm of water")

