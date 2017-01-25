import math
def find_next_square(sq):
          if (math.sqrt(sq) == int(math.sqrt(sq))):
            return int(pow((math.sqrt(sq) + 1), 2))
          else:
            return -1
			