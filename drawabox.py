def draw_square(size):
    a = size * "#" + "\n"
    b = ("#" + ((size - 2) * " ") + "#") + "\n"
    
    c = size * "#"
    d = a + (b * (size - 2)) + c
    return d
	
	