import math
def sctc(sin):
      #print sin
      arr = []
      # get sine, cos, tan, cotan
      sin1 = sin
      
     
      # tan^2 = sin^2 n / (1 - sin^2 n)
      try:
        tan = math.sqrt((sin1 * sin1)/(1-(sin1 * sin1)))
        tan1 = round(tan, 2)
        print "tan: {}".format(tan1)
        
        
      except:
        print 0.0
        
      # cos^2 = 1 / (1 + tan^2 n)
      try:
        cos = math.sqrt(1 / (1 + (tan * tan)))
        print "cos: {}".format(cos)
      except:
        print 0.0
      # cotan = 1/tan
      
      try:
        cotan = (1/ tan)
        print "cotan: {}".format(cotan)
      except:
        print 0.0
           
        
      return
