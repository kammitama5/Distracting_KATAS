import math
def cup_volume(d1, d2, height):
    radius = d1 / 2.0 
    radius1 = d2 / 2.0
    Vol = math.pi * height * ((radius * radius) + (radius1 * radius1) + (radius * radius1)) / 3.0
    return round(Vol, 2)
	
	