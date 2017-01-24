import math
def square_it(digits):
      
      #print (pow(int(math.sqrt(len(str(digits)))),2))
      #print len(str(digits)) 
      
      if (len(str(digits)) == 1):
        print str(digits)
      elif (pow(int(math.sqrt(len(str(digits)))),2)) == len(str(digits)):
         a = int(math.sqrt(len(str(digits)))) 
         print a 
         b = len(str(digits))
         print b / a
      else:
        print "Not a perfect square!"
      return 
	  