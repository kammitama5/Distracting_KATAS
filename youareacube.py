import math
def you_are_a_cube(cube):
        a = math.pow(cube, 1.0/3.0)
        b = round(a, 2) 
        if b * b * b == cube:
          return True
        else:
          return False
		  