import math
def dating_range(age):
      if (age > 14):
        minn = int((age / 2) + 7)
        maxx = int((age - 7) * 2)
      else:
        minn = int((age - 0.10 * age))
        maxx = int((age + 0.10 * age))
    
      return "{}-{}".format(minn,maxx)
      