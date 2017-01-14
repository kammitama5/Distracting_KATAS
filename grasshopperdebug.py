def weather_info (temperature):
    c = (temperature - 32) * (5.0/9.0)
    if (c < 0):
        print ("{} is freezing temperature".format(c))
    else:
        print ( "{} is above freezing temperature".format(c))
    
def convertToCelsius (temperature):
  celsius = (temperature - 32) * (5.0/9.0)
  print celsius
  
  
  
weather_info(50)
weather_info(23)
