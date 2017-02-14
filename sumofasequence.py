def sequence_sum(begin_number, end_number, step):
    count = 0
    for i in range(begin_number, end_number+1, step):
        count = count + i
    return count
	
	