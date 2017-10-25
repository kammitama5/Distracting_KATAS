def elevator_distance(array):
    # use list comprehension
    arr = [array[i - 1] - array[i] for i in range(1, len(array))]
    total = 0
    
    for i in arr:
      total = total + abs(i)
    return total
	
	