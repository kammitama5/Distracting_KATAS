def find_average(array):
    total = 0
    if len(array) == 0:
        return 0
    else:
        length = len(array)
    
    avg = (sum(array) * 1.0) / (length * 1.0)
    return avg
	
	