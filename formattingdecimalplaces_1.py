def two_decimal_places(number):
          a = round (number, 4)
          a1 = str(a)
          if a1[-4] == '.':
            return float((a1)[:-1])
          else:
            a = round (number, 4)
            a2 = a1[:-2]
            return float(a2)
			
			