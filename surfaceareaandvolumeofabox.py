def get_size(w,h,d):
    arr = []
    surface = (2 * w * h) + (2 * d * h) + (2 * w * d)
    volume = (w * h * d)
    arr.insert(0, surface)
    arr.insert(1, volume)
    
    return arr
	
	