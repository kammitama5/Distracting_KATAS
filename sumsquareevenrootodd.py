def sum_square_even_root_odd(nums):
    # your code goes here
    import math
    arr = []
    count = 0
    for i in nums:
        if i % 2 == 0:
            arr.append(math.pow(i, 2.0))
        else:
            arr.append(math.sqrt(i))
    for j in arr:
        count = count + j
    return round((count * 100 / 100.0),2)
	
	