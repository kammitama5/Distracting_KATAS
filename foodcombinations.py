def actually_really_good(foods):
        if len(foods) <= 0:
          return "You know what's actually really good? Nothing!" 
        elif len(foods) == 1:
          a = foods[0][0].upper() + foods[0][1:]
          return "You know what's actually really good? {} and more {}.".format(a, a.lower())
        elif len(foods) >= 1:
          a = foods[0][0].upper() + foods[0][1:].lower()
          b = foods[1].lower()
          return "You know what's actually really good? {} and {}.".format(a, b.lower()) 
        