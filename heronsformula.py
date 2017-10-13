def heron(a, b, c):
    import math
    s = (a + b + c) / 2 
    area = (s * ((s - a) * (s - b) * (s - c)))
    return math.sqrt(area)
	